# Flags:
# -s
import pytest
from .pages.product_page import BookPage
from .pages.links import PageLinks
from .pages.links import BookLinks, BookLinksParametrs


def test_guest_can_add_book_to_basket(browser):
    page = BookPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.SHELLCODERS_BOOK_PAGE + BookLinksParametrs.PROMO_NEWYEAR
    )
    page.open()
    page.should_be_clickable_add_to_basket_button()
    page.should_be_quiz_alert()
    page.should_be_names_equal()
    page.should_be_price_equal()


def test_guest_can_add_other_book_to_basket(browser):
    page = BookPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE + BookLinksParametrs.PROMO_NEWYEAR19
    )
    page.open()
    page.add_product_to_basket()


@pytest.mark.parametrize('parameter', BookLinksParametrs.PROMO_OFFERS)
def test_guest_can_add_product_to_basket(browser, parameter):
    page = BookPage(
        browser, PageLinks.CATALOGUE_URL + BookLinks.CODERS_AT_WORK_BOOK_PAGE + parameter
    )
    page.open()
    page.add_product_to_basket()
