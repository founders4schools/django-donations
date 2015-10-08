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
    api_url = settings.JUST_GIVING_API_URL
    app_id = settings.JUST_GIVING_APP_ID

    def get_exit_url(self, verify_uri):
        if self.donation_status == 'Unverified':
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
        donation_id = request.query_params.get('donation_id', '')
        # raise
        url = '{host}/{appId}/v1/donation/{donationId}'.format(host=self.api_url,
                                                               appId=self.app_id,
                                                               donationId=donation_id)
        resp = requests.get(url, headers={"Content-Type": "application/json"})
        data = resp.json()
        print data
        if data['thirdPartyReference'] == str(self.donation):
            self.donation.status = data['status']
            if data['status'] == "Accepted":
                # assert on the amount ?
                assert self.donation.amount.amount == data['donorLocalAmount']
                self.donation.message = data['message']
                self.donation.est_tax_reclaim = data.get('estimatedTaxReclaim', 0)
                self.donation.provider_source = data['source']
                self.donation.local_amount = data['donorLocalAmount'], data['donorLocalCurrencyCode']
                if data['donorLocalCurrencyCode'] != data['currencyCode']:
                    self.donation.amount = data['amount'], data['currencyCode']
                self.donation.provider_ref = data['donationRef']
                self.donation.save()
                return True
            self.donation.save()
        return False

# {
#     "amount": "2.00",
#     "currencyCode": "GBP",
#     "donationDate": "\/Date(1444216076464+0000)\/",
#     "donationRef": null,
#     "donorDisplayName": "Awesome Guy",
#     "donorLocalAmount": "2.75",
#     "donorLocalCurrencyCode": "EUR",
#     "donorRealName": "Peter Queue",
#     "estimatedTaxReclaim": 0.56,
#     "id": 1234,
#     "image": "",
#     "message": "Hope you like my donation. Rock on!",
#     "source": "SponsorshipDonations",
#     "status": "Accepted",
#     "thirdPartyReference": "1234-my-sdi-ref"
# }
