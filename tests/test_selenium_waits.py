from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_alert_after_5_seconds(waits_driver, wait):
    waits_driver.find_element(By.CSS_SELECTOR, "#alert").click()
    is_alert_shown = wait.until(EC.alert_is_present())

    assert is_alert_shown


def test_change_text_to_selenium_webdriver(waits_driver, wait):
    waits_driver.find_element(By.CSS_SELECTOR, "#populate-text").click()
    element = waits_driver.find_element(By.CSS_SELECTOR, ".target-text")
    previous_text = element.text
    wait.until(lambda _: element.text != previous_text)

    assert "Selenium Webdriver" in element.text


def test_display_button_after_10_sec(waits_driver, wait):
    waits_driver.find_element(By.CSS_SELECTOR, "#display-other-button").click()
    button = waits_driver.find_element(By.CSS_SELECTOR, "#hidden")
    is_button_shown = wait.until(lambda _: button.is_displayed())

    assert is_button_shown


def test_enable_button_after_10_sec(waits_driver, wait):
    waits_driver.find_element(By.CSS_SELECTOR, "#enable-button").click()
    button = waits_driver.find_element(By.CSS_SELECTOR, "#disable")
    is_button_clickable = wait.until(EC.element_to_be_clickable(button))

    assert is_button_clickable


def test_check_checkbox_after_10_sec(waits_driver, wait):
    waits_driver.find_element(By.CSS_SELECTOR, "#checkbox").click()
    checkbox = waits_driver.find_element(By.CSS_SELECTOR, "#ch")
    is_checkbox_checked = wait.until(lambda _: checkbox.is_selected())

    assert is_checkbox_checked
