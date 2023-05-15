import time
import math
import pytest
from logPass import login, password
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Флаги для запуска.
#  -s выводить в консоль принты,
#  -v выводить полный отчёт.

class TestAuthAlien():

    assertMessage = ""

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
    # Передаем в параметрах фикстуру browser из файла conftest.py
    def test_login_stepik(self, browser, link):
        browser.get(link)
        condition = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
        )
        if condition:
            log_button = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
            log_button.click()

            mail_field = browser.find_element(By.ID, "id_login_email")
            mail_field.send_keys(login)

            pass_field = browser.find_element(By.ID, "id_login_password")
            pass_field.send_keys(password)

            log_button_alert = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
            log_button_alert.click()

            # Блок для отлавливания solve again
            try:
                browser.implicitly_wait(7)
                button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
                button_again.click()

            except NoSuchElementException:
                print("\nMissing \"Solve Again\" button")

            finally:
                WebDriverWait(browser, 15).until(
                    EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
                )
                answer_field = browser.find_element(By.TAG_NAME, "textarea")
                answer_field.send_keys(str(math.log(int(time.time()))))

                browser.implicitly_wait(10)
                submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
                submit_button.click()

                result = WebDriverWait(browser, 15).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "p.smart-hints__hint")
                    ))
                if result.text != "Correct!":
                    self.assertMessage += result.text
                    print(self.assertMessage)
                assert result.text == "Correct!"


if __name__ == "__main__":
    pytest.main()
