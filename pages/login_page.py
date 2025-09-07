from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_form.send_keys(password)
        password_form_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_form_confirm.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()