import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    # Находим значение х на странице
    value = calc(int(browser.find_element(By.CSS_SELECTOR, "#input_value").text))
    # Находим поле для заполнения и вставляем посчитанное значение
    input_fild = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_fild.send_keys(value)
    # Находим чекбокс "I'm the robot" и нажимаем его
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    # Находим радиобатн и выбираем значение "Robots rule"
    radiobutt = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutt.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)
