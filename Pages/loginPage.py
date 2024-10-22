from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    button_CustomerLogin_xpath = "//button[contains(.,'Customer Login')]"
    dropdown_CustomerName_id = "userSelect"
    button_Login_xpath = "//button[contains(.,'Login')]"
    dropdown_AccountNumber_id = "accountSelect"
    button_Deposit_xpath_xpath = "//button[contains(.,'Deposit')]"
    textbox_DepositAmount_xpath = "//input[@placeholder='amount']"
    button_submit_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        customerLoginElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_CustomerLogin_xpath)))
        customerLoginElement.click()

    def enterCustomerName(self, customer1):
        wait = WebDriverWait(self.driver, 10)
        customerNameElement = wait.until(EC.visibility_of_element_located((By.ID, self.dropdown_CustomerName_id)))
        customerNameElement.send_keys(customer1)

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        loginButtonElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Login_xpath)))
        loginButtonElement.click()

    def enterAccountNumber(self, accountNumber1):
        wait = WebDriverWait(self.driver, 10)
        customerAccountNumberElement = wait.until(EC.visibility_of_element_located
                                                  ((By.ID, self.dropdown_AccountNumber_id)))
        customerAccountNumberElement.send_keys(accountNumber1)

    def clickDepositButton(self):
        wait = WebDriverWait(self.driver, 10)
        depositButtonElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Deposit_xpath_xpath)))
        depositButtonElement.click()

# Try and use faker
# def enterDepositAmount(self, AccNumber1):
#   wait = WebDriverWait(self.driver, 10)
#    depositAmountElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.textbox_DepositAmount_xpath )))
#    depositAmountElement.send_keys(AccNumber1)

# button_submit_xpath
