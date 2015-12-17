# -*- coding: utf-8 -*-
__version__ = '0.2.7'
__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])

def setup():
    from .models import load_providers, load_frequencies
    load_providers()
    load_frequencies()

default_app_config = 'donations.apps.DonationConfig'
