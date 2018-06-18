from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import app_settings as settings
from .forms import DonationForm
from .models import Donation, Frequency
from .providers.just_giving import SimpleDonationProvider as JustGivingProvider
from .serializers import DonationSerializer


class DonateAPI(APIView):

    def post(self, request):
        # take the required parameters and create the model
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            ser = serializer.save()
            if self.request.user.is_authenticated:
                ser.donor = self.request.user
                ser.save()
            url = reverse(settings.VERIFY_API_URL_NAME, kwargs={'pk': ser.id})
            verify_uri = request.build_absolute_uri(url)
            redirect_uri = ser.donate(verify_uri)
            return HttpResponseRedirect(redirect_uri)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)


class DonateView(CreateView):
    model = Donation
    form_class = DonationForm

    def form_valid(self, form):
        self.object = form.save()
        if self.request.user.is_authenticated:
            self.object.donor = self.request.user
            self.object.save()
        url = reverse(settings.VERIFY_API_URL_NAME, kwargs={'pk': self.object.id})
        verify_uri = self.request.build_absolute_uri(url)
        redirect_uri = self.object.donate(verify_uri)
        return HttpResponseRedirect(redirect_uri)

    def get_initial(self):
        finished_uri = self.request.build_absolute_uri(self.set_finished_uri())
        return {
            "finished_uri": finished_uri,
        }

    def get_context_data(self, **kwargs):
        context = super(DonateView, self).get_context_data(**kwargs)
        frequency_ids = Frequency.objects.values_list('id', flat=True)
        context.update({
            'monthly_id': frequency_ids.filter(name__iexact="monthly").first(),
            'single_id': frequency_ids.filter(name__iexact="single").first(),
            'monthly_url': self.get_monthly_url(),
        })
        return context

    def set_finished_uri(self):
        """This is the URL where the provider redirects once the donation is completed"""
        return settings.VERIFY_FINISHED_URL

    def get_monthly_url(cls):
        return JustGivingProvider.get_monthly_url()


class VerifyAPI(APIView):

    def get(self, request, pk):
        # TODO: url probably needs to be passed through to model/verify method
        donation = Donation.objects.get(pk=pk)
        if donation.status == Donation.Statuses.UNVERIFIED and not donation.is_verified:
            # verify it
            donation.verify_donation(request)
        # return redirect + unverfied or verified
        scheme, netloc, path, query_string, frag = urlsplit(donation.finished_uri)
        query_params = parse_qs(query_string)
        query_params['verified'] = [donation.is_verified]
        query_params['ref'] = donation.get_provider().donation_reference()
        url = urlunsplit((scheme, netloc, path, urlencode(query_params, doseq=True), frag))
        return HttpResponseRedirect(url)
