# -*- coding: utf-8 -*-
'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES_DEBUG = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!bs^+tns(^i@m#n9thbtvr%cqqueildau@u62q4ib%pjjdzh7)b')

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'



# Your local stuff: Below this line define 3rd party library settings

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())


# JUST_GIVING_WEB_URL = 'http://v3-sandbox.justgiving.com'
# JUST_GIVING_API_URL = 'http://api-sandbox.justgiving.com'
# # JUST_GIVING_CHARITY_ID = '265263' # founders4schools id
# JUST_GIVING_CHARITY_ID = '2050' # demo id
# JUST_GIVING_APP_ID = '7caeb2c2'
#
# DONATION_PROVIDERS = {
#     'Just Giving': 'just_giving.SimpleDonationProvider'
# }
# DONATION_FREQUENCIES = {
#     'one-off': '0 days',
# }
# CURRENCIES = ['GBP', 'EUR', 'AUD', 'USD', 'ZAR', 'CAD', 'AED', 'HKD', 'SGD']
