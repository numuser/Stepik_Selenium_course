from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert str(self.browser.current_url).find('login'), "~~~ Wrong login page link ~~~"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "~~~ Login form is not presented ~~~"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "~~~ Register form is not presented ~~~"
