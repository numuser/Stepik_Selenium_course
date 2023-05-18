from .base_page import BasePage
from .locators import BookPageLocators


class BookPage(BasePage):

    def should_be_clickable_add_to_basket_button(self):
        assert self.is_element_clickable(
            *BookPageLocators.ADD_TO_BASKET_BTN
        ), "~~~ Busket button isn't presented! ~~~"

    def should_be_quiz_alert(self):
        assert self.solve_quiz_and_get_code(

        ), "~~~ Quiz alert isn't presented or not solved! ~~~"

    def should_be_names_equal(self):
        assert self.is_element_present(
            *BookPageLocators.BOOK_NAME
        ), "~~~ Book name isn't presented! ~~~"

        assert self.is_element_present(
            *BookPageLocators.BASKET_ITEM_NAME
        ), "~~~ Basket item name price isn't presented! ~~~"

        book_name = self.browser.find_element(*BookPageLocators.BOOK_NAME).text
        basket_item_name = self.browser.find_element(*BookPageLocators.BASKET_ITEM_NAME).text

        assert book_name == basket_item_name,\
            "~~~ Basket item name and book name isn't equal! ~~~"

    def should_be_price_equal(self):
        assert self.is_element_present(
            *BookPageLocators.BOOK_PRICE
        ), "~~~ Book price isn't presented! ~~~"

        assert self.is_element_present(
            *BookPageLocators.BASKET_TOTAL_PRICE
        ), "~~~ Basket total price isn't presented! ~~~"

        book_price = self.browser.find_element(*BookPageLocators.BOOK_PRICE).text
        basket_total = self.browser.find_element(*BookPageLocators.BASKET_TOTAL_PRICE).text

        assert book_price == basket_total,\
            "~~~ Basket total price and book price isn't equal! ~~~"
