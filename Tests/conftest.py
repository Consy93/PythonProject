import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser.lower == "edge":
        driver = webdriver.Edge()
    elif browser.lower == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
