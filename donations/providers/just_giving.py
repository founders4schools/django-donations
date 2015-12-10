'Just Giving Provider for Donations'

from __future__ import unicode_literals
try:
    from urllib import quote_plus, urlencode
except ImportError: # Python 3
    from urllib.parse import quote_plus, urlencode
import logging
import requests

from donations.providers.base import DonationProvider
from donations import app_settings

logger = logging.getLogger(__name__)


class SimpleDonationProvider(DonationProvider):

    charity_id = app_settings.JUST_GIVING_CHARITY_ID
    web_url = app_settings.JUST_GIVING_WEB_URL
    api_url = app_settings.JUST_GIVING_API_URL
    app_id = app_settings.JUST_GIVING_APP_ID

    def get_exit_url(self, verify_uri):
        if self.donation_status == 'Unverified':
            return '{0}?donation_id=JUSTGIVING-DONATION-ID'.format(quote_plus(verify_uri))
        return quote_plus(self.donation.redirect_uri)

    def donate(self, verify_uri):
        query_params = {
            'currency': self.get_currency(),
            'amount': self.get_value(),
            'exitUrl': self.get_exit_url(verify_uri),
            'reference': self.donation_reference()
        }
        uri = '{0}/4w350m3/donation/direct/charity/{1}?{2}'.format(self.web_url, self.charity_id, urlencode(query_params))
        return uri

    def donation_reference(self):
        return str(self.donation.id)

    def verify(self, request):
        donation_id = request.GET.get('donation_id', '')
        url = '{host}/{appId}/v1/donation/{donationId}'.format(host=self.api_url,
                                                               appId=self.app_id,
                                                               donationId=donation_id)
        resp = requests.get(url, headers={"Content-Type": "application/json"})
        data = resp.json()
        logger.info("JustGiving - Verifying with data = %s", data)
        if data['thirdPartyReference'] == self.donation_reference():
            self.donation.status = data['status']
            if data['status'] == "Accepted":
                self.donation.message = data.get('message', '')
                self.donation.est_tax_reclaim = data.get('estimatedTaxReclaim', 0)
                self.donation.provider_source = data.get('source', None)
                self.donation.set_local_amount(data.get('donorLocalAmount', None),
                                               data.get('donorLocalCurrencyCode', None))
                self.donation.set_amount(data.get('amount', None),
                                         data.get('currencyCode', None))
                self.donation.provider_ref = data.get('donationRef', None)
                self.donation.donor_display_name = data.get('donorDisplayName', None)
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
