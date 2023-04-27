from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = ChromeDriverManager().install()
driver = webdriver.Chrome(executable_path=path)
driver.get('https://suninjuly.github.io/text_input_task.html')

with webdriver.Chrome() as browser:
    browser.get("https://suninjuly.github.io/cats.html")


