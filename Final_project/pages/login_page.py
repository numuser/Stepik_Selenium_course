from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.implicitly_wait(4)
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)
        register_button.click()

    def should_be_login_page(self):
        assert str(self.browser.current_url).find('login'), "~~~ Wrong login page link! ~~~"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "~~~ Login form is not presented! ~~~"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "~~~ Register form is not presented! ~~~"



