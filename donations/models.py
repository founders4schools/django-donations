# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import logging
from importlib import import_module

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from djmoney.models.fields import MoneyField

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class Frequency(models.Model):
    """Frequency of donations, how often they repeat"""
    name = models.CharField(max_length=100)
    interval = models.DurationField()

    class Meta:  # pylint: disable=C1001
        verbose_name_plural = 'Frequencies'

    def __str__(self):
        return "{0} ({1})".format(self.name, self.interval)


@python_2_unicode_compatible
class DonationProvider(models.Model):
    """External provider that handle the donations"""

    name = models.CharField(max_length=100, default='BlankProvider')
    description = models.CharField(max_length=255, default='')
    klass = models.CharField(max_length=255, default='')

    def get_provider_class(self):
        """get the class of the donation provider.
        I have hardcoded the first bit to prevent any module being imported"""
        module_name, klass_name = self.klass.rsplit('.', 1)
        module = import_module('donations.providers.{0}'.format(module_name))
        return getattr(module, klass_name)

    def __str__(self):
        return self.name


DONATION_SOURCE = ["DirectDonations", "SponsorshipDonations", "Ipdd", "Sms"]
DONATION_SOURCE = [(i, i) for i in DONATION_SOURCE]

DONATION_STATUSES = ["Accepted", "Rejected", "Cancelled", "Refunded", "Pending", "Unverified"]
DONATION_STATUSES = [(i, i) for i in DONATION_STATUSES]


@python_2_unicode_compatible
class Donation(models.Model):
    """(Abstract representation of a Donation)"""

    # https://github.com/django-money/django-money
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    provider = models.ForeignKey(DonationProvider, related_name='donations')
    frequency = models.ForeignKey(Frequency, related_name='donations')
    datetime = models.DateTimeField(default=timezone.now)
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='donations')
    donor_display_name = models.CharField(blank=True, null=True, max_length=255,
                                          help_text="display name returned by the provider")
    status = models.CharField(default='Unverified', choices=DONATION_STATUSES, max_length=50)
    is_verified = models.BooleanField(default=False)
    finished_uri = models.URLField(blank=True)

    provider_ref = models.CharField(blank=True, max_length=100)
    local_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    message = models.CharField(blank=True, null=True, max_length=255)
    est_tax_reclaim = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    provider_source = models.CharField(blank=True, null=True, max_length=50, choices=DONATION_SOURCE,
                                       help_text="source of the donation from within a provider")

    def __str__(self):
        if self.local_amount:
            return "{0} at {1}".format(self.local_amount, self.datetime.strftime('%Y/%m/%d %H:%M:%S'))
        return "{0} at {1}".format(self.amount, self.datetime.strftime('%Y/%m/%d %H:%M:%S'))

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

    def set_money_field(self, field, tuple_content):
        for content in tuple_content:
            if not content:
                logger.warning("Not setting field %s: incomplete data provided %s", field, tuple_content)
                return
        setattr(self, field, tuple_content)

    def set_amount(self, value, currency):
        self.set_money_field('amount', (value, currency))

    def set_local_amount(self, value, currency):
        self.set_money_field('local_amount', (value, currency))
