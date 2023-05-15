import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://SunInJuly.github.io/execute_script.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    browser.execute_script("document.title='Script executing';alert('Robots at work')")
    alert = browser.switch_to.alert
    time.sleep(10)



