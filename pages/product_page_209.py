from .base_page import BasePage
from .locators import ProductPage209Locators
from selenium.webdriver.common.by import By

class ProductPage209(BasePage):

    def basket_find_and_click(self):
        button = self.browser.find_element(*ProductPage209Locators.BASKET_BUTTON)
        button.click()

    def check_guest_cant_see_success_message_after_adding_product_to_cart(self):
        assert self.is_not_element_present(*ProductPage209Locators.PRODUCT_NAME_IN_BASKET), "Проверяем, что нет сообщения об успехе с помощью is_not_element_present"

    def check_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPage209Locators.PRODUCT_NAME_IN_BASKET), "Проверяем, что нет сообщения об успехе с помощью is_not_element_present"

    def check_message_disappeared_after_adding_product_to_cart(self):
        assert self.is_disappeared(*ProductPage209Locators.PRODUCT_NAME_IN_BASKET), "Проверяем, что нет сообщения об успехе с помощью is_disappeared"
        time.sleep(1)