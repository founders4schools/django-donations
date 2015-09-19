'Just Giving Provider for Donations'

from .base import DonationProvider
import requests
from django.conf import settings

class SimpleDonationProvider(DonationProvider):

    def __init__(self, *args, **kwargs):
        pass

    def donate(self):
        pass

    def verify(self):
        pass
