import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_LOGIN_FORM)
        password = self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FORM)
        confirm_password = self.driver.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FORM)
        registration_button = self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password.send_keys("cpUser123")
        confirm_password.send_keys("cpUser123")
        registration_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.driver.current_url
        assert "login" in cur_url, "Miss login word in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missed"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is missed"
