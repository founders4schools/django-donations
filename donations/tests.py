import unittest

from django.test import TestCase


class NoddyTestCase(TestCase):

    def test_long_nose(self):
        self.assertEqual(1+1, 2)
