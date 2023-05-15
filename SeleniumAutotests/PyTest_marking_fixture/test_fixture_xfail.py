import pytest
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.mainpage
class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")


@pytest.mark.otherpage
class TestOtherPage1():

    @pytest.mark.xfail(strict=True)
    def test_succeed(self):
        assert True

    @pytest.mark.xfail()
    def test_not_succeed(self):
        assert False

    @pytest.mark.skip
    def test_skipped(self):
        assert False
