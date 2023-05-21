import math
from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser: Remote, link, timeout=10):
        """ Base class the web page

        :param browser: Selenium WebDriver instance
        :param link: Link to the page
        :param timeout: Time to wait before raise in seconds
        """
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        """ Give web page in the browser

        :return: None
        """
        self.browser.get(self.link)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "User icon is not presented, probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login button is not presented"

    def is_element_present(self, how_search, what_search: str):
        """ Return True if element is present, else False

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

    def is_not_element_present(self, how_search, what_search, timeout=4):
        """

        :param how_search: By.CSS_SELECTOR, By.ID, etc.
        :param what_search: Selector
        :param timeout: Time to wait before raise in seconds
        :return: bool
        """
        try:
            WebDriverWait(
                self.browser, timeout).until(
                EC.presence_of_element_located((how_search, what_search))
            )

        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how_search, what_search, timeout=4):
        """

        :param how_search: By.CSS_SELECTOR, By.ID, etc.
        :param what_search: Selector
        :param timeout: Time to wait before raise in seconds
        :return: bool
        """
        try:
            WebDriverWait(
                self.browser, timeout, 1, TimeoutException
            ).until_not(EC.presence_of_element_located((how_search, what_search))
                        )
        except TimeoutException:
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
            btn = self.browser.find_element(how_search, what_search)
            btn.click()
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        self.browser.implicitly_wait(5)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("\nNo second alert presented")
            return False
        return True
