import pytest
from selenium import webdriver


@pytest.fixture
def common_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def actions_driver(common_driver):
    common_driver.implicitly_wait(10)
    common_driver.get("https://the-internet.herokuapp.com/")
    yield common_driver


@pytest.fixture
def waits_driver(common_driver):
    common_driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
    yield common_driver
