from selenium import webdriver
from selenium.webdriver.common.by import By
import time

links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
for link in links:

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
        time.sleep(1)

        welcome_txt = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == welcome_txt
        time.sleep(5)
