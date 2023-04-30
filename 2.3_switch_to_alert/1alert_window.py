import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/alert_accept.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

    alert_accept = browser.switch_to.alert
    alert_accept.accept()

    xValue = browser.find_element(By.ID, "input_value")
    answer = calc(int(xValue.text))
    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    print(browser.switch_to.alert.text.split()[-1])

