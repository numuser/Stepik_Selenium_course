import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects2.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    result = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    print(result)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(5)
