

from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.urlresolvers import reverse, resolve
from urlparse import urlsplit, urlunsplit, parse_qs
from urllib import urlencode

from django.http import HttpResponseRedirect

from .models import Donation, DonationProvider
from .serializers import DonationSerializer

class DonateAPI(APIView):
    def post(self, request, format=None):

        # take the required parameters and create the model
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            ser = serializer.save()

            verify_uri = request.build_absolute_uri(reverse('donations:api:verify', kwargs={'id': ser.id}))
            redirect_uri = ser.donate(verify_uri)
            return HttpResponseRedirect(redirect_uri)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)


class DonateView(CreateView):
    model = Donation

    def form_valid(self, form):
        self.object = form.save()
        verify_uri = self.request.build_absolute_uri(reverse('donations:api:verify', kwargs={'id': self.object.id}))
        redirect_uri = self.object.donate(verify_uri)
        return HttpResponseRedirect(redirect_uri)

    def get_context_data(self, **kwargs):
        context = super(DonateView, self).get_context_data(**kwargs)
        context['form'].fields['finished_uri'].initial = self.request.build_absolute_uri(self.set_finished_uri())
        return context

    def set_finished_uri(self):
        'This should be overridden with logic for unique url'
        return '/'


class VerifyAPI(APIView):
    def get(self, request, id, format=None):
        # TODO: url probably needs to be passed through to model/verify method
        donation = Donation.objects.get(pk=id)
        if donation.verify and not donation.is_verified:
            # verify it
            donation.verify_donation(request)
        # return redirect + unverfied or verified
        scheme, netloc, path, query_string, frag = urlsplit(donation.finished_uri)
        query_params = parse_qs(query_string)
        query_params['verified'] = [donation.is_verified]
        url = urlunsplit((scheme, netloc, path, urlencode(query_params, doseq=True), frag))
        return HttpResponseRedirect(url)
