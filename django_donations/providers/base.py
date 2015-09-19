'Base Provider for provding donations'



class DonationProvider(object):

    def donate(self):
        'make the api calls to give money'
        raise NotImplementedError

    def verify(self):
        'Optional method to verify donation has been successfully recieved'
        raise NotImplementedError
