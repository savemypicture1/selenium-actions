from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkboxes(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(6) a").click()
    checkbox_1 = driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]:nth-child(1)')
    checkbox_1.click()
    checkbox_2 = driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]:nth-child(3)')
    checkbox_2.click()

    assert checkbox_1.get_attribute("checked") == "true"
    assert checkbox_2.get_attribute("checked") != "true"


def test_context_menu(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(7) a").click()
    area = driver.find_element(By.CSS_SELECTOR, "#hot-spot")
    action = ActionChains(driver)
    action.context_click(area).perform()
    alert = driver.switch_to.alert
    alert.accept()

    assert 1


def test_dropdown(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(11) a").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, "#dropdown")
    select = Select(dropdown)
    select.select_by_value("2")

    assert dropdown.get_attribute("value") == "2"


def test_entry_ad(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(15) a").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer p")))
    driver.find_element(By.CSS_SELECTOR, ".modal-footer p").click()
    driver.find_element(By.CSS_SELECTOR, "a#restart-ad").click()
    wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "#modal")))
    modal = driver.find_element(By.CSS_SELECTOR, "#modal")

    assert modal.value_of_css_property("display") == "block"


def test_form_authentication(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(21) a").click()
    username_field = driver.find_element(By.CSS_SELECTOR, "#username")
    password_field = driver.find_element(By.CSS_SELECTOR, "#password")
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, ".fa-sign-in").click()

    assert driver.find_element(By.CSS_SELECTOR, ".flash.success")


def test_frames(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(22) a").click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/iframe"]').click()
    iframe_element = driver.find_element(By.CSS_SELECTOR, "#mce_0_ifr")
    driver.switch_to.frame(iframe_element)
    text_field = driver.find_element(By.CSS_SELECTOR, "#tinymce")
    text_field.click()
    text_field.clear()
    text_field.send_keys("Hello World!")

    assert "Hello World!" in text_field.text


def test_horizontal_slider(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(24) a").click()
    slider = driver.find_element(By.CSS_SELECTOR, 'input[type="range"]')
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider, 50, 0).perform()
    for i in range(3):
        slider.send_keys(Keys.ARROW_LEFT)

    assert slider.get_attribute("value") == "3"


def test_hovers(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(25) a").click()
    figure = driver.find_element(By.CSS_SELECTOR, ".figure:nth-child(4)")
    action = ActionChains(driver)
    action.move_to_element(figure).perform()
    figure.find_element(By.CSS_SELECTOR, ".figcaption a").click()
    result = driver.find_element(By.CSS_SELECTOR, "h1").text

    assert "Not Found" in result


def test_inputs(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(27) a").click()
    input = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
    input.click()
    input.send_keys("0123456789")

    assert "0123456789" in input.get_attribute("value")


def test_key_presses(driver):
    driver.find_element(By.CSS_SELECTOR, "#content li:nth-child(31) a").click()
    input = driver.find_element(By.CSS_SELECTOR, "#target")
    result = driver.find_element(By.CSS_SELECTOR, "#result")
    input.click()
    input.send_keys(Keys.BACK_SPACE)

    assert "BACK_SPACE" in result.text
