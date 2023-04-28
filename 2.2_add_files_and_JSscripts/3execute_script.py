from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    xValue = browser.find_element(By.ID, "input_value")
    answer = calc(int(xValue.text))

    # Прокручиваем страницу на сто пикселей вниз, что бы поле было видно

    # """Как вариант еще можно скрывать ненужный элемент

    # browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
    # Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body

    # from selenium.webdriver.common.keys import Keys

    # browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх"""

    browser.execute_script("window.scrollBy(0, 100);")
    answerField = browser.find_element(By.ID, "answer")
    answerField.send_keys(answer)

    chkBox = browser.find_element(By.ID, "robotCheckbox")
    chkBox.click()
    radiobutt = browser.find_element(By.ID, "robotsRule")
    radiobutt.click()

    submitButton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(5)

