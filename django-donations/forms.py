'Mixins to make creating donations easy - here is the restriction on choices for amounts, not in the model'


from django.forms import Form, ModelForm


class FreeFormDonationFormMixin(ModelForm):
    pass


class FixedDonationFormMixin(ModelForm):
    pass

# etc
