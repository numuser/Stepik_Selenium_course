from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

with webdriver.Chrome(executable_path=ChromeDriverManager().install()) as browser:
    browser.get(link)

    req_inputs = browser.find_elements(By.CSS_SELECTOR, "input:required")

    for inp in req_inputs:
        inp.send_keys("aboba")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)

    welcome_txt = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_txt
    time.sleep(10)
