

SETTINGS = {
    'INSTALLED_APPS': [
        'django.contrib.auth',
        'rest_framework',
        'south',
        'donations'
    ],
    'DONATION_FREQUENCIES' : {
        'single': '0 days',
    },
    'DONATION_PROVIDERS': {
        'Just Giving': 'just_giving.SimpleDonationProvider'
    }
}
