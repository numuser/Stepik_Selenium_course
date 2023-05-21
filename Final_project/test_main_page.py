# Flags:
# -v --tb=line
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.links import PageLinks


def test_guest_can_go_to_login_page(browser):
    # 1. Open homepage
    # 2. Go to login page
    # 3. Expect login page

    page = MainPage(browser, PageLinks.MAIN_PAGE_URL)
    page.open()
    page.go_to_login_page()


def test_should_see_login_link(browser):
    # 1. Open homepage
    # 2. Check login button visibility
    # 3. Expect login button

    page = MainPage(browser, PageLinks.MAIN_PAGE_URL)
    page.open()
    page.should_be_login_link()  # проверяем видимость кнопки логина


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # 1. Open homepage
    # 2. Go to the cart by clicking the button in the header of the site
    # 3. We expect there are no items in the cart
    # 4. We expect that there is a text that the cart is empty

    page = BasketPage(browser, PageLinks.MAIN_PAGE_URL)
    page.open()
    page.go_to_basket_page()
    page.is_not_contain_any_in_basket()
    page.is_basket_empty_message()
