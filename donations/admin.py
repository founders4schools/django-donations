'Admin for donations'


from django.contrib import admin
from .models import Donation, Frequency, DonationProvider

class DonationAdmin(admin.ModelAdmin):
    pass

class FrequencyAdmin(admin.ModelAdmin):
    pass

class DonationProviderAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'klass')

admin.site.register(Donation, DonationAdmin)
admin.site.register(Frequency, FrequencyAdmin)
admin.site.register(DonationProvider, DonationProviderAdmin)
