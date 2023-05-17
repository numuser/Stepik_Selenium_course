import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(autouse=True)  # выполняется для каждой функции
def prepare_date():
    print("\npreparing some critical data for every test")


class TestMainPage1():
    # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
