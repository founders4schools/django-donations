# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from donations.forms import DonationForm


class FixedDonationForm(DonationForm):
    amounts = [1, 5, 10, 10000]
