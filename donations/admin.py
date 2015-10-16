from django.contrib import admin
from donations.models import Donation, Frequency, DonationProvider


class DonationAdmin(admin.ModelAdmin):
    list_display = ('amount', 'provider', 'frequency', 'datetime', 'donor', 'is_verified')


class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'interval')


class DonationProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'klass')


admin.site.register(Donation, DonationAdmin)
admin.site.register(Frequency, FrequencyAdmin)
admin.site.register(DonationProvider, DonationProviderAdmin)
