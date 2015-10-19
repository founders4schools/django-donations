
from django.conf import settings

JUST_GIVING_WEB_URL = getattr(settings, 'JUST_GIVING_WEB_URL', 'http://v3-sandbox.justgiving.com')
JUST_GIVING_API_URL = getattr(settings, 'JUST_GIVING_API_URL', 'http://api-sandbox.justgiving.com')
# JUST_GIVING_CHARITY_ID = '265263' # founders4schools id
JUST_GIVING_CHARITY_ID = getattr(settings, 'JUST_GIVING_CHARITY_ID', '2050')  # demo id
JUST_GIVING_APP_ID = getattr(settings, 'JUST_GIVING_APP_ID', 'XXXXX')
# JUST_GIVING_APP_ID = '7caeb2c2'

CURRENCIES = getattr(settings, 'CURRENCIES', ['GBP', 'EUR', 'AUD', 'USD', 'ZAR', 'CAD', 'AED', 'HKD', 'SGD'])

DONATION_FREQUENCIES = getattr(settings, 'DONATION_FREQUENCIES', {})
DONATION_PROVIDERS = getattr(settings, 'DONATION_PROVIDERS', {})
