from django.apps import AppConfig

class DonationConfig(AppConfig):
    name = 'donation'
    verbose_name = "Django Donations"
    def ready(self):
        from .models import load_providers, load_frequencies
        load_providers()
        load_frequencies()
