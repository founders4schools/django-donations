from django.conf import settings

JUST_GIVING_WEB_URL = getattr(settings, 'JUST_GIVING_WEB_URL', 'http://v3-sandbox.justgiving.com')
JUST_GIVING_API_URL = getattr(settings, 'JUST_GIVING_API_URL', 'http://api-sandbox.justgiving.com')
JUST_GIVING_CHARITY_ID = getattr(settings, 'JUST_GIVING_CHARITY_ID', '2050')  # demo id
JUST_GIVING_APP_ID = getattr(settings, 'JUST_GIVING_APP_ID', 'XXXXX')

CURRENCIES = getattr(settings, 'CURRENCIES', ['GBP', 'EUR', 'AUD', 'USD', 'ZAR', 'CAD', 'AED', 'HKD', 'SGD'])

VERIFY_API_URL_NAME = getattr(settings, 'DONATION_VERIFY_API_URL_NAME', 'donations:api:verify')

VERIFY_FINISHED_URL = getattr(settings, 'DONATION_VERIFY_FINISHED_URL', '/donate/thanks/')
