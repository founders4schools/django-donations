DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqlite3'
    },
}
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'south',
    'donations'
]
ROOT_URLCONF = 'django_autoconfig.autourlconf'
# from django_autoconfig.autoconfig import configure_settings
# configure_settings(globals())
