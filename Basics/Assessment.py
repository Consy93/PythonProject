import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()  # This starts the session
driver.maximize_window()
driver.get("http://www.way2automation.com/angularjs-protractor/banking/#/login")
time.sleep(3)

driver.find_element(By.XPATH, "//button[contains(.,'Customer Login')]").click()
time.sleep(3)
driver.find_element(By.ID, "userSelect").click()






