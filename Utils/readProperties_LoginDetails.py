import configparser

config = configparser.RawConfigParser()
config.read('./Configuration/loginDetails.ini')


class ReadLoginConfig():

    def getBankingURL(self):
        return config.get("URL", "bankingURL")

    def getCustomerName(self):
        return config.get("Customer Names", "customer1")

    def getAccountNumber(self):
        return config.get("Account Number", "accountNumber1")


