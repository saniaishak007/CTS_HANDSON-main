from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.lambdatest.com/selenium-playground"


def test_simple_form_submission(driver):
    driver.get(BASE_URL + "/simple-form-demo")

    message = "Hello Selenium"

    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-message"))
    )
    input_box.clear()
    input_box.send_keys(message)

    submit_button = driver.find_element(By.ID, "showInput")
    submit_button.click()

    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert output.text == message


def test_checkbox_demo(driver):
    driver.get(BASE_URL + "/checkbox-demo")

    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[type='checkbox']")
        )
    )

    checkbox.click()
    assert checkbox.is_selected()

    checkbox.click()
    assert not checkbox.is_selected()