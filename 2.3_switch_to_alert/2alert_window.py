import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/redirect_accept.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    subButton = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    subButton.click()

    # Переход на вторую вкладку и выбор ее основной
    newWindow = browser.window_handles[1]
    browser.switch_to.window(newWindow)

    xValue = browser.find_element(By.ID, "input_value")
    answer = calc(int(xValue.text))
    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    print(browser.switch_to.alert.text.split()[-1])

    print(browser.switch_to.alert.text.split()[-1])
