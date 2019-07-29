from .base_page import BasePage # импорт базового класса BasePage из файла basepage.py
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):   # этот класс наследник basepage
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"