import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class BasePage():
    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self, how_search, what_search: str):
        """
        :param how_search: By.CSS_SELECTOR, By.ID, etc.
        :param what_search: Selector
        :return: bool
        """
        try:
            self.browser.implicitly_wait(5)
            self.browser.find_element(how_search, what_search)
        except NoSuchElementException:
            return False
        return True

    def is_element_clickable(self, how_search, what_search):
        """
        :param how_search: By.CSS_SELECTOR, By.ID, etc.
        :param what_search: Selector
        :return: bool
        """
        try:
            self.browser.implicitly_wait(5)
            self.browser.find_element(how_search, what_search).click()
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        self.browser.implicitly_wait(5)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            return False
        return True
