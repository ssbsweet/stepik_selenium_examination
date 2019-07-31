from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def basket_find_and_click(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def check_name_on_page_and_in_basket(self):
        name1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        name2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert name1.text == name2.text, "Наименование в корзине отличается от наименования товара on page"

    def check_price_on_page_and_in_basket(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)
        price2 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert price1.text == price2.text, "Цена в корзине отличается от цены товара"

