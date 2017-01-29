# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from donations.models import Donation, Frequency, DonationProvider


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('amount', 'provider', 'frequency', 'datetime', 'donor', 'is_verified')


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'interval')


@admin.register(DonationProvider)
class DonationProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'klass')
