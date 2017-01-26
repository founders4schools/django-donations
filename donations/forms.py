# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.forms import ModelForm, URLField, HiddenInput, Select
from djmoney.forms.fields import MoneyField
from djmoney.forms.widgets import MoneyWidget

from donations.models import Donation


class DonationForm(ModelForm):
    finished_uri = URLField(widget=HiddenInput())

    class Meta:  # pylint: disable=C1001
        model = Donation
        fields = ('amount', 'provider', 'frequency', 'finished_uri')

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        if hasattr(self, 'amounts'):
            self.amounts = [(i, i) if type(i) in [int, float] else i for i in self.amounts]
            donate_widget = MoneyWidget(amount_widget=Select(choices=self.amounts))
            self.fields['amount'] = MoneyField(currency_widget=donate_widget)
