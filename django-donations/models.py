'models.py for django-donations'

from django.db import models



class Donation(models.Model):
    """(Abstract representation of a Model)"""

    amount - float/int? (django-money)
    currency - django-money
    provider - foreign key
    frequency - foreign key
    datetime
    user (optional)
    referral_url (optional) (just giving)

    def __unicode__(self):
        return u"Donation"



class Frequency(models.Model):
    """(Frequency description)"""

    name
    delta? - this should be celery compatible - should allow for one off vs repeat


    def __unicode__(self):
        return u"Frequency"


# based on settings auto create db entries? so user does not need to repeat entering info?

class DonationProvider(models.Model):
    """(DonationProvider description)"""

    name
    description
    code

    def __unicode__(self):
        return u"DonationProvider"
