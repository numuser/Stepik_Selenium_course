import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/explicit_wait2.html"
with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(By.ID, "book")
    condition = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    if condition:
        button.click()

        xValue = browser.find_element(By.ID, "input_value")
        answer = calc(int(xValue.text))
        answerField = browser.find_element(By.ID, "answer")
        answerField.send_keys(answer)

        submit_button = browser.find_element(By.ID, "solve")
        scrollToButt = ActionChains(browser)
        scrollToButt.move_to_element(submit_button)
        submit_button.click()

        print(browser.switch_to.alert.text.split()[-1])
