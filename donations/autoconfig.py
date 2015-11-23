from django import get_version
SETTINGS = {
    'INSTALLED_APPS': [
        'django.contrib.auth',
        'rest_framework',
        'donations'
    ],
    'DONATION_FREQUENCIES': {
        'single': '0 days',
    },
    'DONATION_PROVIDERS': {
        'Just Giving': 'just_giving.SimpleDonationProvider'
    },
}


if get_version() < '1.7':
    SETTINGS['INSTALLED_APPS'].insert(0,'south')
