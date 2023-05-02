from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


link = "https://suninjuly.github.io/file_input.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    inpName = browser.find_element(By.CSS_SELECTOR, "[name=\"firstname\"]")
    inpName.send_keys("Negretta")
    inpLastname = browser.find_element(By.CSS_SELECTOR, "[name=\"lastname\"]")
    inpLastname.send_keys("Pidoreska")
    inpMail = browser.find_element(By.CSS_SELECTOR, "[name=\"email\"]")
    inpMail.send_keys("test@testmail.com")

    # Получаем текущий путь до исполняемого файла
    # Находим текстовый файл на отправку
    # И отправляем методом send_keys()
    curDir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(curDir, "biba.txt")
    uplFile = browser.find_element(By.ID, "file")
    uplFile.send_keys(filePath)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)

