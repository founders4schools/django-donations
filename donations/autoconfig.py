

SETTINGS = {
    'JUST_GIVING_WEB_URL' : 'http://v3-sandbox.justgiving.com',
    'JUST_GIVING_API_URL' : 'http://api-sandbox.justgiving.com',
    # JUST_GIVING_CHARITY_ID = '265263' # founders4schools id
    'JUST_GIVING_CHARITY_ID' : '2050', # demo id
    'JUST_GIVING_APP_ID' : '7caeb2c2',

    'DONATION_PROVIDERS' : {
        'Just Giving': 'just_giving.SimpleDonationProvider'
    },
    'DONATION_FREQUENCIES' : {
        'one-off': '0 days',
    },
    'CURRENCIES' : ['GBP', 'EUR', 'AUD', 'USD', 'ZAR', 'CAD', 'AED', 'HKD', 'SGD'],
}
