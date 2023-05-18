# Flags:
# -s
from .pages.product_page import BookPage
from .pages.links import PageLinks
from .pages.links import BookPageParametrs


def test_guest_can_add_product_to_basket(browser):
    page = BookPage(
        browser, PageLinks.SHELLCODERS_BOOK_URL+BookPageParametrs.SHELLCODERS_BOOK_PAGE_PROMO_NEWYEAR)
    page.open()
    page.should_be_clickable_add_to_basket_button()
    page.should_be_quiz_alert()
    page.should_be_names_equal()
    page.should_be_price_equal()
