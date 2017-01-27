# -*- coding: utf-8
from django.apps import AppConfig


class DonationsConfig(AppConfig):
    name = 'donations'
    verbose_name = "Django Donations"

    def ready(self):
        from .config_loaders import load_providers, load_frequencies
        load_providers()
        load_frequencies()
