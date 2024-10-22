import time
import allure
import pytest

from Pages.loginPage import LoginPage
from Utils.readProperties_LoginDetails import ReadLoginConfig


class Test_TestOne:
    bankingURL = ReadLoginConfig().getBankingURL()
    customer1 = ReadLoginConfig().getCustomerName()
    accountNumber1 = ReadLoginConfig().getAccountNumber()

    @pytest.mark.consy
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTestsOne(self, setup):
        self.driver = setup
        self.driver.get(self.bankingURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickCustomerLoginButton()
        self.login.enterCustomerName(self.customer1)
        self.login.clickLoginButton()
        self.login.enterAccountNumber(self.accountNumber1)
        self.login.clickDepositButton()
