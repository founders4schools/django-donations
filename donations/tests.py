from django.test import TestCase
from .models import Donation, DonationProvider, Frequency
from .providers.just_giving import SimpleDonationProvider


class ModelTest(TestCase):

    def test_frequency(self):
        Frequency.objects.create(name='single', interval='0 days')
        self.assertEqual(Frequency.objects.count(), 1)

    def test_provider(self):
        provider = DonationProvider.objects.create(
            name='Just Giving',
            description='Just Giving Provider',
            klass='just_giving.SimpleDonationProvider',
        )
        self.assertEqual(DonationProvider.objects.count(), 1)
        provider_class = provider.get_provider_class()
        self.assertEqual(provider_class, SimpleDonationProvider)


class DonationTest(TestCase):

    def setUp(self):
        self.frequency = Frequency.objects.create(name='single', interval='0 days')
        self.provider = DonationProvider.objects.create(
            name='Just Giving',
            description='Just Giving Provider',
            klass='just_giving.SimpleDonationProvider',
        )

    def test_create(self):
        Donation.objects.create(amount=10, provider=self.provider, frequency=self.frequency)
        self.assertEqual(Donation.objects.count(), 1)
