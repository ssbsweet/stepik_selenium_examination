from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_basket(self):
        basket_button = self.driver.find_element(*MainPageLocators.BASKET_LINK)
        basket_button.click()
