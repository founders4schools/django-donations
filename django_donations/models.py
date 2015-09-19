'models.py for django-donations'

from django.db import models
import moneyed
from djmoney.models.fields import MoneyField

from timedelta.fields import TimedeltaField

from django.contrib.auth import get_user_model
from datetime import datetime
from importlib import import_module

class Frequency(models.Model):
    """(Frequency description)"""
    class Meta:
        verbose_name_plural = 'Frequencies'
    name = models.CharField(max_length=100)
    # this should be a duration field native in 1.8
    interval = TimedeltaField() # this should be celery compatible - should allow for one off vs repeat

    def __unicode__(self):
        return u"{} ({})".format(self.name, self.interval)


# based on settings auto create db entries? so user does not need to repeat entering info?

class DonationProvider(models.Model):
    """(DonationProvider description)"""

    name = models.CharField(max_length=100, default='BlankProvider')
    description = models.CharField(max_length=255, default='')
    klass = models.CharField(max_length=255, default='')

    def get_provider_class(self):
        module_name, klass_name = self.klass.rsplit('.', 1)
        module = import_module(module_name)
        return getattr(module, klass_name)

    def get_provider(self):
        pass

    def __unicode__(self):
        return self.name

class Donation(models.Model):
    """(Abstract representation of a Model)"""

    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    provider = models.ForeignKey(DonationProvider)
    frequency = models.ForeignKey(Frequency)
    datetime = models.DateTimeField(default=datetime.now)
    donor = models.ForeignKey(get_user_model(), blank=True, null=True)
    # referral_url (optional) (just giving exit url)

    def __unicode__(self):
        return u"{} - {}".format(self.donor, self.datetime)

    def donate(self):
        pass
