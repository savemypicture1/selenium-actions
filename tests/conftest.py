import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://the-internet.herokuapp.com/?ref=hackernoon.com")
    yield driver
    driver.quit()
