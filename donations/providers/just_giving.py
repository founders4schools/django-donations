'Just Giving Provider for Donations'

from .base import DonationProvider
import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
from django.conf import settings
from urllib import quote_plus
import logging

logger = logging.getLogger(__name__)

class SimpleDonationProvider(DonationProvider):

    charity_id = settings.JUST_GIVING_CHARITY_ID
    web_url = settings.JUST_GIVING_WEB_URL

    def get_exit_url(self):
        if self.verify_donation:
            return '{}?donation_id=JUSTGIVING-DONATION-ID'.format(quote_plus(self.donation.redirect_uri))
        return quote_plus(self.donation.redirect_uri)

    def donate(self):
        query_params = {
            'currency': self.get_currency(),
            'amount': self.get_value(),
            'exitUrl': self.get_exit_url(),
            'reference': unicode(self.donation)
        }
        uri = '{}/{}'.format(self.web_url, self.charity_id)
        try:
            resp = requests.post(uri, query_params)
        except ConnectionError, exp:
            logger.error('Connection Error: %s', exp.message)
            return
        except HTTPError, exp:
            logger.error('Invalid Response: %s', exp.message)
            return
        except Timout:
            logger.error('Request to %s Timed out.', uri)
            return
        if resp.ok:
            logger.info('Donation made to JustGiving')
            logger.debug(response.raw)
            return True
        return False


    def verify(self):
        # TODO
        return True
