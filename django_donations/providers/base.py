'Base Provider for provding donations'



class DonationProvider(object):

    def __init__(self, donation):
        self.amount = donation.amount
        self.currency = donation.currency
        self.verify_donation = donation.verify

    def get_value(self):
        return self.amount.amount

    def get_currency(self):
        return self.currency

    def donate(self):
        'make the api calls to give money'
        raise NotImplementedError

    def verify(self):
        'Optional method to verify donation has been successfully recieved'
        raise NotImplementedError
