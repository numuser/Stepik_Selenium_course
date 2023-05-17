from selenium.common.exceptions import NoSuchElementException


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
            self.browser.find_element(how_search, what_search)
        except NoSuchElementException:
            return False
        return True
