# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.test import TestCase

from donations.config_loaders import load_frequencies, load_providers
from donations.models import Frequency, DonationProvider


class DefaultSetupTest(TestCase):
    def test_load_frequencies(self):
        self.assertEqual(Frequency.objects.count(), 0)
        load_frequencies()
        self.assertEqual(Frequency.objects.count(), 1)

    def test_load_providers(self):
        self.assertEqual(DonationProvider.objects.count(), 0)
        load_providers()
        self.assertEqual(DonationProvider.objects.count(), 1)
