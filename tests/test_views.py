# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from compat import reverse
from django.test import TestCase


class DonateViewTest(TestCase):
    def test_get_donation_normal(self):
        response = self.client.get(reverse('testapp:index'))
        self.assertContains(response, "Donate Now")

    def test_get_donation_fixed(self):
        response = self.client.get(reverse('testapp:fixed'))
        self.assertContains(response, "Donate Now")

    def test_get_donation_thank_you(self):
        response = self.client.get(reverse('testapp:thank-you'))
        self.assertContains(response, "Thank You for your donation")
