from .base_page import BasePage # импорт базового класса BasePage из файла basepage.py
from .login_page import LoginPage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

    def go_to_basket(self):
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        basket_button.click()

    def basket_is_empty(self):
        assert self.is_element_present(*MainPageLocators.SOMETHING_IN_BASKET), "Basket is not empted"