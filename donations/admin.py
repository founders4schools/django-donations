from django.contrib import admin

from donations.models import Donation, Frequency


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("amount", "frequency", "datetime", "donor", "is_verified")


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ("name", "interval")
