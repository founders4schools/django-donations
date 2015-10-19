from donations.forms import DonationForm


class MyDonationForm(DonationForm):
    pass


class MyFixedDonationForm(DonationForm):
    amounts = [1, 5, 10, 10000]
