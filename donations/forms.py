'Mixins to make creating donations easy - here is the restriction on choices for amounts, not in the model'


from django.forms import Form, ModelForm, URLField, HiddenInput, ChoiceField, Select
from .models import Donation
from djmoney.forms.widgets import MoneyWidget, CURRENCY_CHOICES
from djmoney.forms.fields import MoneyField

class DonationForm(ModelForm):
    finished_uri = URLField(widget=HiddenInput())

    class Meta:
        model = Donation
        fields = ('amount', 'provider', 'frequency', 'finished_uri')

    def __init__(self, *args, **kwargs):
        super(DonationFormMixin, self).__init__(*args, **kwargs)
        if hasattr(self, 'amounts'):
            self.amounts = [(i, i) if type(i) in [int, float] else i for i in self.amounts ]
            # currency_field = ChoiceField(choices=CURRENCY_CHOICES)
            donate_widget = MoneyWidget(amount_widget=Select(choices=self.amounts))
            self.fields['amount'] = MoneyField(currency_widget=donate_widget)
