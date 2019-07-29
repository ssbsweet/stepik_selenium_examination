from .base_page import BasePage # импорт базового класса BasePage из файла basepage.py
from selenium.webdriver.common.by import By

class MainPage(BasePage):   # этот класс наследник basepage
    def go_to_login_page(self):
        login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link.click()