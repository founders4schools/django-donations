# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.test import TestCase


class DonateViewTest(TestCase):
    def test_get_donation_normal(self):
        response = self.client.get(reverse('testapp:index'))
        self.assertContains(response, "Donate Now")
