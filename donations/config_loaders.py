# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import logging

from donations import app_settings

logger = logging.getLogger(__name__)


def load_frequencies():
    """Make sure the frequencies defined in settings are loaded in database"""
    frequencies = app_settings.DONATION_FREQUENCIES
    logger.debug('Loading Donation Frequencies')
    from donations.models import Frequency
    for name, period in frequencies.items():
        try:
            dp, created = Frequency.objects.get_or_create(name=name, interval=period)
            if created:
                logger.info('Loaded %s with interval of %s', name, period)
            else:
                logger.info('Frequency %s with interval of %s already exists', name, period)
        except Exception as exc:
            logger.warning("Could not load the Frequency model instance due to %s", exc)


def load_providers():
    """Make sure the providers defined in settings are loaded in database"""
    providers = app_settings.DONATION_PROVIDERS
    logger.debug('Loading Donation Providers')
    from donations.models import DonationProvider
    for name, klass in providers.items():
        try:
            dp, created = DonationProvider.objects.get_or_create(name=name, klass=klass)
            if created:
                logger.info('Loaded %s called %s', klass, name)
            else:
                logger.info('Provider %s called %s already exists', klass, name)
        except Exception as exc:
            logger.warning("Could not load the DonationProvider model instance due to %s", exc)
