# Flags:
# -v --tb=line
import time
import pytest
from .pages.product_page import BookPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.links import PageLinks, BookLinks
from .pages.links import BookLinksParametrs


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(
            browser, PageLinks.LOGIN_PAGE_URL
        )
        page.open()
        mail = str(time.time())
        page.register_new_user(mail + "@fakemail.org", mail + "password")
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # 1. Open product page
        # 2. Add product to basket
        # 3. Send keys and accept alert
        # 4. Expect book names are equal
        # 5. Expect prices are equal

        page = BookPage(
            browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE + BookLinksParametrs.PROMO_NEWYEAR19
        )
        page.open()
        page.add_to_basket()
        page.should_be_quiz_alert()
        page.should_be_names_equal()
        page.should_be_price_equal()

    def test_user_cant_see_success_message(self, browser):
        page = BookPage(
            browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE
        )
        page.open()
        page.should_not_success_alert()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # 1. Open product page
    # 2. Add product to basket
    # 3. Send keys and accept alert
    # 4. Expect number in console as answer

    page = BookPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.SHELLCODERS_BOOK_PAGE + BookLinksParametrs.PROMO_NEWYEAR
    )
    page.open()
    page.add_product_to_basket_with_quiz_alert()


@pytest.mark.skip
@pytest.mark.xfail(reason="no second alert presented -> a website issue")
@pytest.mark.parametrize('parameter', BookLinksParametrs.PROMO_OFFERS)
def test_guest_can_add_all_product_to_basket(browser, parameter):
    page = BookPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE + parameter
    )
    page.open()
    page.add_product_to_basket_with_quiz_alert()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = BookPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE
    )
    page.open()
    page.add_to_basket()
    page.should_not_success_alert()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = BookPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE
    )
    page.open()
    page.add_to_basket()
    page.should_message_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # 1. Open product page
    # 2. Go to the cart by clicking the button in the header of the site
    # 3. Expect there are no items in the cart
    # 4. Expect there is a text that the cart is empty

    page = BasketPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE
    )
    page.open()
    page.go_to_basket_page()
    page.is_not_contain_any_in_basket()
    page.is_basket_empty_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # 1. Open product page
    # 2. Go to login page
    # 3. We expect link be login page
    page = LoginPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.SHELLCODERS_BOOK_PAGE
    )
    page.open()  # открываем страницу
    page.go_to_login_page()
    page.should_be_login_page()  # выполняем метод страницы — проверяем ссылку на страницу логина
