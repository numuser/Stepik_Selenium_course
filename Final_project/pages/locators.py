from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.ID, "login-link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class BookPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_ITEM_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
