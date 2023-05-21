from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[@id=\"default\"]/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    CONTENT_SHEET = (By.ID, "messages")


class BookPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_ITEM_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class LoginPageLocators():
    LOGIN_LINK = (By.ID, "login-link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn.btn-lg")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
