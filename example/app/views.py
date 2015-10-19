from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from donations.views import DonateView

from .forms import MyDonationForm, MyFixedDonationForm


class ExampleDonateView(DonateView):
    template_name = "index.html"
    form_class = MyDonationForm

    def set_finished_uri(self):
        return reverse('myapp:thank-you')


class ExampleFixedDonateView(DonateView):
    template_name = "index.html"
    form_class = MyFixedDonationForm
    amounts = [2, 4, 5, 60]

    def set_finished_uri(self):
        return reverse('myapp:thank-you')


class ExampleThankYouView(TemplateView):
    template_name = "thank_you.html"
