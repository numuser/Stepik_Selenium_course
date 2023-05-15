import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationForm(unittest.TestCase):
    # *Позже дописать цикл для вызова test_form*
    links = ["https://suninjuly.github.io/registration1.html", "https://suninjuly.github.io/registration2.html"]

    def test_form1(self, link="https://suninjuly.github.io/registration1.html"):
        with webdriver.Chrome() as browser:
            browser.get(link)

            req_input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
            req_input1.send_keys("sus")
            req_input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
            req_input2.send_keys("sus")
            req_input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
            req_input3.send_keys("sus")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            # ждем загрузки страницы
            condition = WebDriverWait(browser, 2).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Congratulations! You have successfully "
                                                                      "registered!")
            )
            if condition:

                welcome_txt = browser.find_element(By.TAG_NAME, "h1").text
                assert "Congratulations! You have successfully registered!" == welcome_txt

    def test_form2(self):
        self.test_form1(link="https://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()
