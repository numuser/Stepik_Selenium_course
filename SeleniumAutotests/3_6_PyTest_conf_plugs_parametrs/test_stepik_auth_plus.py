import time
import math
import pytest
from logPass import login, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def answer_calc():
    return str(math.log(int(time.time())))


class TestAuthAlien():

    message = ""

    links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1",
             ]

    @pytest.mark.parametrize("link", links)
    def test_login_stepik(self, browser, link):
        browser.get(link)
        answer = answer_calc()
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


            answer_condition = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "ember86")))
            if answer_condition:
                answer_field = browser.find_element(By.ID, "ember86")
                answer_field.send_keys(answer)

