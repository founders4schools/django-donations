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
            frequency, created = Frequency.objects.get_or_create(name=name, interval=period)
            status = "New" if created else "Existing"
            logger.debug("%s frequency %s loaded", status, frequency)
        except Exception as exc:
            logger.warning("Could not load the Frequency model instance due to %s", exc)
