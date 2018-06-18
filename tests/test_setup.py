from django.test import TestCase

from donations.config_loaders import load_frequencies
from donations.models import Frequency


class DefaultSetupTest(TestCase):
    def test_load_frequencies(self):
        self.assertEqual(Frequency.objects.count(), 0)
        load_frequencies()
        self.assertEqual(Frequency.objects.count(), 1)
