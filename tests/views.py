# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from donations.forms import DonationForm
from donations.views import DonateView
from tests.forms import FixedDonationForm


class SimpleDonateView(DonateView):
    template_name = "index.html"
    form_class = DonationForm

    def set_finished_uri(self):
        return reverse('testapp:thank-you')


class FixedDonateView(DonateView):
    template_name = "index.html"
    form_class = FixedDonationForm
    amounts = [2, 4, 5, 60]

    def set_finished_uri(self):
        return reverse('testapp:thank-you')


class DonateThankYouView(TemplateView):
    template_name = "thank_you.html"
