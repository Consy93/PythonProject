
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    button_CustomerLogin_xpath = "//button[contains(.,'Customer Login')]"
    dropdown_CustomerName_id = "userSelect"
    button_Login_xpath = "//button[contains(.,'Login')]"


def __init__(self, driver):
    self.driver = driver

def clickCustomerLoginButton(self):
    wait = WebDriverWait(self.driver,10)
    customerLoginElement = wait.until(EC.visibility_of_element_located(By.XPATH, self.button_CustomerLogin_xpath))
    customerLoginElement.click()
