from datetime import timedelta

from django.conf import settings

JUST_GIVING_WEB_URL = getattr(settings, 'JUST_GIVING_WEB_URL', 'http://v3-sandbox.justgiving.com')
JUST_GIVING_API_URL = getattr(settings, 'JUST_GIVING_API_URL', 'http://api-sandbox.justgiving.com')
JUST_GIVING_CHARITY_ID = getattr(settings, 'JUST_GIVING_CHARITY_ID', '2050')  # demo id
JUST_GIVING_APP_ID = getattr(settings, 'JUST_GIVING_APP_ID', 'XXXXX')

CURRENCIES = getattr(settings, 'CURRENCIES', ['GBP', 'EUR', 'AUD', 'USD', 'ZAR', 'CAD', 'AED', 'HKD', 'SGD'])

DONATION_FREQUENCIES = getattr(settings, 'DONATION_FREQUENCIES', {
    'single': timedelta(days=0),
})
DONATION_PROVIDERS = getattr(settings, 'DONATION_PROVIDERS', {
    'Just Giving': 'just_giving.SimpleDonationProvider'
})
VERIFY_API_URL_NAME = getattr(settings, 'DONATION_VERIFY_API_URL_NAME', 'donations:api:verify')
