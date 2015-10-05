'Signals - should have a post save to make the donation'
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Donation


# @receiver(pre_save, sender=Donation)
# def donation_pre_save_handler(sender, instance, **kwargs):
#     donated = instance.donate()
#     if not donated:
#         # cancels save model not created
#         raise NotDonatedException

#     elif donated and instance.verify and not instance.is_verified:
#         instance.verify_donation()

# @receiver(post_save, sender=Donation)
# def donation_post_save_handler(sender, instance, **kwargs):
#     if instance.verify and not instance.is_verified:
#         instance.verify_donation()


# post /donate/ with amount, currency
# this should redirect to jg.com/
# do jq.com redirect back to /verify/
# verify does the verify of donation ;)
