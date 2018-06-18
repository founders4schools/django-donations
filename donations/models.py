import logging

from django.conf import settings
from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

from .providers.just_giving import SimpleDonationProvider as JustGivingProvider

logger = logging.getLogger(__name__)


class Frequency(models.Model):
    """Frequency of donations, how often they repeat"""
    name = models.CharField(max_length=100)
    interval = models.DurationField()

    class Meta:  # pylint: disable=C1001
        verbose_name_plural = 'Frequencies'

    def __str__(self):
        return "{0} ({1})".format(self.name, self.interval)


class Donation(models.Model):
    """(Abstract representation of a Donation)"""
    SOURCE_CHOICES = [
        ("DirectDonations", "Direct Donations"),
        ("SponsorshipDonations", "Sponsorship Donations"),
        ("Ipdd", "IPDD"),
        ("Sms", "SMS"),
    ]

    class Statuses:
        ACCEPTED = "Accepted"
        REJECTED = "Rejected"
        CANCELLED = "Cancelled"
        REFUNDED = "Refunded"
        PENDING = "Pending"
        UNVERIFIED = "Unverified"
        CHOICES = [
            (ACCEPTED, "Accepted"),
            (REJECTED, "Rejected"),
            (CANCELLED, "Cancelled"),
            (REFUNDED, "Refunded"),
            (PENDING, "Pending"),
            (UNVERIFIED, "Unverified"),
        ]

    # https://github.com/django-money/django-money
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    frequency = models.ForeignKey(Frequency, related_name='donations', on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='donations',
                              on_delete=models.CASCADE)
    donor_display_name = models.CharField(
        blank=True, null=True, max_length=255,
        help_text="display name returned by the provider",
    )
    status = models.CharField(default=Statuses.UNVERIFIED, choices=Statuses.CHOICES, max_length=50)
    is_verified = models.BooleanField(default=False)
    finished_uri = models.URLField(blank=True)

    provider_ref = models.CharField(blank=True, max_length=100)
    local_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='GBP')
    message = models.CharField(blank=True, null=True, max_length=255)
    est_tax_reclaim = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    provider_source = models.CharField(
        blank=True, null=True, max_length=50, choices=SOURCE_CHOICES,
        help_text="source of the donation from within a provider"
    )

    def __str__(self):
        if self.local_amount:
            return "{0} at {1}".format(self.local_amount, self.datetime.strftime('%Y/%m/%d %H:%M:%S'))
        return "{0} at {1}".format(self.amount, self.datetime.strftime('%Y/%m/%d %H:%M:%S'))

    def get_provider(self):
        """Hook to enable retrieving another provider"""
        return JustGivingProvider(self)

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
