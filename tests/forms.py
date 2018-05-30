from donations.forms import DonationForm


class FixedDonationForm(DonationForm):
    amounts = [1, 5, 10, 10000]
