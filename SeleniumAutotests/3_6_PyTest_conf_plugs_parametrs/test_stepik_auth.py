import time
from logPass import login, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://stepik.org/lesson/236895/step/1"


class TestAuth():

    def test_login_stepik(self, browser):
        browser.get(link)
        condition = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ember33"))
        )
        if condition:
            log_button = browser.find_element(By.ID, "ember33")
            log_button.click()

            mail_field = browser.find_element(By.ID, "id_login_email")
            mail_field.send_keys(login)

            pass_field = browser.find_element(By.ID, "id_login_password")
            pass_field.send_keys(password)

            log_button_alert = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
            log_button_alert.click()


