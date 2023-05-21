from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_MESSAGE
        ), "~~~ Basket empty message isn't present! ~~~"

    def is_not_contain_any_in_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.CONTENT_SHEET
        ), "~~~ Basket not empty! ~~~"


