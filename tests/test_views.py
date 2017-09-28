# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from compat import reverse
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase

from donations.models import Frequency, DonationProvider, Donation

User = get_user_model()


class DonateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.f = Frequency.objects.create(
            name='single',
            interval=timedelta(days=0)
        )
        cls.p = DonationProvider.objects.create(
            name='Just Giving',
            klass='just_giving.SimpleDonationProvider'
        )
        cls.donor = User.objects.create_user(
            username='generous-helper',
            email='helper@donate.com',
            password="I'm being kind",
        )

    def test_get_donation_normal(self):
        response = self.client.get(reverse('testapp:index'))
        self.assertContains(response, "Donate Now")

    def test_get_donation_fixed(self):
        response = self.client.get(reverse('testapp:fixed'))
        self.assertContains(response, "Donate Now")

    def test_get_donation_thank_you(self):
        response = self.client.get(reverse('testapp:thank-you'))
        self.assertContains(response, "Thank You for your donation")

    def test_get_donate_api(self):
        response = self.client.get(reverse('donations:api:donate'))
        self.assertContains(response, "[]")

    def test_post_donate_api_invalid(self):
        response = self.client.post(reverse('donations:api:donate'), data={})
        self.assertContains(
            response,
            "This field is required.",
            status_code=400,
            count=4
        )

    def test_post_donate_api_minimal(self):
        response = self.client.post(reverse('donations:api:donate'), data={
            'amount': 20,
            'currency': 'GBP',
            'provider': 'Just Giving',
            'frequency': 'single',
        })
        d = Donation.objects.latest('datetime')
        self.assertIsNotNone(d)
        expected_url = (
            "http://v3-sandbox.justgiving.com/4w350m3/donation/direct/charity/2050?"
            "currency=GBP&amount=20.00&"
            "exitUrl=http%253A%252F%252Ftestserver%252Fapi%252Fverify%252F1%3Fdonation_id%3DJUSTGIVING-DONATION-ID"
            "&reference={donation.id}".format(donation=d)
        )
        self.assertRedirects(response, expected_url=expected_url, fetch_redirect_response=False)

    def test_post_api_authenticated(self):
        self.client.login(username='generous-helper', password="I'm being kind")
        self.client.post(reverse('donations:api:donate'), data={
            'amount': 20,
            'currency': 'GBP',
            'provider': 'Just Giving',
            'frequency': 'single',
        })
        d = Donation.objects.latest('datetime')
        self.assertIsNotNone(d)
        self.assertEqual(d.donor, self.donor)

    def test_donate_form_empty_post(self):
        response = self.client.post(reverse('testapp:index'), data={})
        self.assertContains(
            response,
            "This field is required.",
            status_code=200,
            count=4
        )

    def test_donate_form_minimal_post(self):
        response = self.client.post(reverse('testapp:index'), data={
            'amount_0': 20,
            'amount_1': 'GBP',
            'provider': self.p.id,
            'frequency': self.f.id,
            'finished_uri': 'http://testapp.com/thank-you/',
        })
        d = Donation.objects.latest('datetime')
        self.assertIsNotNone(d)
        expected_url = (
            "http://v3-sandbox.justgiving.com/4w350m3/donation/direct/charity/2050?"
            "currency=GBP&amount=20&"
            "exitUrl=http%253A%252F%252Ftestserver%252Fapi%252Fverify%252F1%3Fdonation_id%3DJUSTGIVING-DONATION-ID"
            "&reference={donation.id}".format(donation=d)
        )
        self.assertRedirects(response, expected_url=expected_url, fetch_redirect_response=False)

    def test_donate_form_authenticated_post(self):
        self.client.login(username='generous-helper', password="I'm being kind")
        self.client.post(reverse('testapp:index'), data={
            'amount_0': 20,
            'amount_1': 'GBP',
            'provider': self.p.id,
            'frequency': self.f.id,
            'finished_uri': 'http://testapp.com/thank-you/',
        })
        d = Donation.objects.latest('datetime')
        self.assertIsNotNone(d)
        self.assertEqual(d.donor, self.donor)
