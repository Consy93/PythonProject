import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")


class ReadLoginConfig():
    def getBankingURL(self):
        return config.get("URLS", "bankingURL")
