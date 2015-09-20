'Just Giving Provider for Donations'

from .base import DonationProvider
import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
from django.conf import settings

class SimpleDonationProvider(DonationProvider):

    charity_id = settings.JUST_GIVING_CHARITY_ID
    web_url = settings.JUST_GIVING_WEB_URL

    def donate(self):
        query_params = {
            'currency': self.get_currency(),
            'amount': self.get_value(),
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
        if resp.status_code == 200:
            pass


    def verify(self):
        pass
