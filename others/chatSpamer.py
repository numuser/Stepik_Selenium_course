import time

from selenium import webdriver
from selenium.webdriver.common.by import By

loginlink = "https://vk.com/"
chatlink = ""
with webdriver.Chrome() as browser:
    browser.get(loginlink)
    loginField = browser.find_element(By.ID, "index_email")
    loginField.send_keys(1)
    time.sleep(50)
    chat = browser.find_element(By.ID, "im_editable0")
    for i in range(30):
        chat.send_keys("a")
        time.sleep(1)
