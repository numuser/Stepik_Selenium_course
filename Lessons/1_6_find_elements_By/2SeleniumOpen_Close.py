from selenium import webdriver
from selenium.webdriver.common.by import By


link = ""

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

################################################################

# else we can use 'with' construction
with webdriver.Chrome() as browser:
    pass
