from datetime import timedelta

import requests_mock
from django.test import TestCase

from donations.models import Donation, Frequency
from donations.providers.base import DonationProvider as BaseDonationProvider
from donations.providers.just_giving import SimpleDonationProvider


class DummyRequest(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class ModelTest(TestCase):

    def test_frequency(self):
        f = Frequency.objects.create(name='single', interval=timedelta(days=0))
        self.assertEqual("{0}".format(f), "single (0:00:00)")


class DonationTest(TestCase):

    def setUp(self):
        self.frequency = Frequency.objects.create(name='single', interval=timedelta(days=0))

    def test_create(self):
        d = Donation.objects.create(amount=10, frequency=self.frequency)
        self.assertEqual(Donation.objects.count(), 1)
        self.assertIn("10", "{0}".format(d))

    def test_base_provider(self):
        donation = Donation.objects.create(amount=10, frequency=self.frequency)
        provider = BaseDonationProvider(donation)
        self.assertEqual(provider.get_value(), 10)
        self.assertEqual(str(provider.get_currency()), 'GBP')
        self.assertRaises(NotImplementedError, provider.verify, 'dummy')
        self.assertRaises(NotImplementedError, provider.donate, 'dummy')


class JustGivingProviderTest(TestCase):

    def setUp(self):
        self.frequency = Frequency.objects.create(name='single', interval=timedelta(days=0))
        self.donation = Donation.objects.create(amount=10, frequency=self.frequency)

    def test_donate(self):
        provider = SimpleDonationProvider(self.donation)
        self.assertEqual(provider.get_value(), 10)
        self.assertEqual(str(provider.get_currency()), 'GBP')
        donate_url = provider.donate('/redirect-uri/')
        self.assertIn('http://v3-sandbox.justgiving.com/4w350m3/donation/direct/charity/2050', donate_url)
        self.assertIn('currency=GBP', donate_url)
        self.assertIn('amount=10', donate_url)
        self.assertIn('exitUrl=%252Fredirect-uri%252F%3Fdonation_id%3DJUSTGIVING-DONATION-ID', donate_url)
        self.assertIn('reference=1', donate_url)

    def test_verify(self):
        provider = SimpleDonationProvider(self.donation)
        with requests_mock.mock() as m:
            m.get('http://api-sandbox.justgiving.com/XXXXX/v1/donation/1', json={
                "amount": "2.00",
                "currencyCode": "GBP",
                "donationDate": "\/Date(1444216076464+0000)\/",
                "donationRef": "12345",
                "donorDisplayName": "Awesome Guy",
                "donorLocalAmount": "2.75",
                "donorLocalCurrencyCode": "EUR",
                "donorRealName": "Peter Queue",
                "estimatedTaxReclaim": 0.56,
                "id": 1234,
                "image": "",
                "message": "Hope you like my donation. Rock on!",
                "source": "SponsorshipDonations",
                "status": "Accepted",
                "thirdPartyReference": "1"
            })
            request = DummyRequest(GET={'donation_id': '1'})
            self.assertTrue(provider.verify(request))

    def test_verify_ko(self):
        provider = SimpleDonationProvider(self.donation)
        with requests_mock.mock() as m:
            m.get('http://api-sandbox.justgiving.com/XXXXX/v1/donation/1', json={
                "thirdPartyReference": None
            })
            request = DummyRequest(GET={'donation_id': '1'})
            self.assertFalse(provider.verify(request))
            self.assertEqual(Donation.objects.get(id=1).status, "Unverified")

    def test_verify_not_accepted(self):
        provider = SimpleDonationProvider(self.donation)
        with requests_mock.mock() as m:
            m.get('http://api-sandbox.justgiving.com/XXXXX/v1/donation/1', json={
                "status": "Rejected",
                "thirdPartyReference": "1"
            })
            request = DummyRequest(GET={'donation_id': '1'})
            self.assertFalse(provider.verify(request))
            self.assertEqual(Donation.objects.get(id=1).status, "Rejected")
