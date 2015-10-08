

from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from donations.views import DonateView
from donations.models import Donation
from .forms import MyDonationForm

class ExampleDonateView(DonateView):
    template_name = "index.html"
    form_class = MyDonationForm

    def set_finished_uri(self):
        return reverse('thank-you')

class ExampleThankYouView(TemplateView):
    template_name = "thank_you.html"
