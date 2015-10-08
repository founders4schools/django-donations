'models.py for django-donations'

from django.db import models
import moneyed
from djmoney.models.fields import MoneyField

from timedelta.fields import TimedeltaField

from django.contrib.auth import get_user_model
from datetime import datetime
from importlib import import_module
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class Frequency(models.Model):
    """(Frequency description)"""
    class Meta:
        verbose_name_plural = 'Frequencies'
    name = models.CharField(max_length=100)
    # this should be a duration field native in 1.8
    # https://pypi.python.org/pypi/django-timedeltafield
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
        '''get the class of the donation provider.
        I have hardcoded the first bit to prevent any module being imported'''
        module_name, klass_name = self.klass.rsplit('.', 1)
        module = import_module('donations.providers.{}'.format(module_name))
        return getattr(module, klass_name)

    def __unicode__(self):
        return self.name


class Donation(models.Model):
    """(Abstract representation of a Donation)"""

    # https://github.com/django-money/django-money
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    provider = models.ForeignKey(DonationProvider, related_name='donations')
    frequency = models.ForeignKey(Frequency, related_name='donations')
    datetime = models.DateTimeField(default=datetime.now)
    donor = models.ForeignKey(get_user_model(), blank=True, null=True, related_name='donations')
    verify = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    finished_uri = models.URLField(blank=True)

    def __unicode__(self):
        return u"{} at {}".format(self.amount, self.datetime.strftime('%Y/%m/%d %H:%M:%S'))

    def get_provider(self):
        return self.provider.get_provider_class()(self)

    def get_value(self):
        return self.amount.amount

    def get_currency(self):
        return self.amount.currency

    def donate(self, verify_uri):
        return self.get_provider().donate(verify_uri)

    def verify_donation(self, request):
        self.is_verified = self.get_provider().verify(request)
        self.save()


def load_frequencies():
    frequencies = getattr(settings, 'DONATION_FREQUENCIES', {})
    logger.info('Loading Donation Frequencies')
    for name, period in frequencies.items():
        dp, created = Frequency.objects.get_or_create(name=name, interval=period)
        if created:
            logger.info('Loaded %s with interval of %s', name, period)
        else:
            logger.info('Frequency %s with interval of %s already exists', name, period)

def load_providers():
    providers = getattr(settings, 'DONATION_PROVIDERS', {})
    logger.info('Loading Donation Providers')
    for name, klass in providers.items():
        dp, created = DonationProvider.objects.get_or_create(name=name, klass=klass)
        if created:
            logger.info('Loaded %s called %s', klass, name)
        else:
            logger.info('Provider %s called %s already exists', klass, name)

load_providers()
load_frequencies()
