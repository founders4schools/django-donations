'Just Giving Provider for Donations'

from .base import DonationProvider
import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
from django.conf import settings
from urllib import quote_plus, urlencode
import logging

logger = logging.getLogger(__name__)

class SimpleDonationProvider(DonationProvider):

    charity_id = settings.JUST_GIVING_CHARITY_ID
    web_url = settings.JUST_GIVING_WEB_URL

    def get_exit_url(self, verify_uri):
        if self.verify_donation:
            return '{}?donation_id=JUSTGIVING-DONATION-ID'.format(quote_plus(verify_uri))
        return quote_plus(self.donation.redirect_uri)

    def donate(self, verify_uri):
        query_params = {
            'currency': self.get_currency(),
            'amount': self.get_value(),
            'exitUrl': self.get_exit_url(verify_uri),
            'reference': unicode(self.donation)
        }
        uri = '{}/4w350m3/donation/direct/charity/{}?{}'.format(self.web_url, self.charity_id, urlencode(query_params))
        return uri


    def verify(self, request):
        # TODO
        url = 'https://api.justgiving.com/{appId}/v1/donation/{donationId}'
        return True
