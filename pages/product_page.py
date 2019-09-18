from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Add to basket button isn't presented"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element not disappeared, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def add_item_to_basket(self):
        add_item = self.driver.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_item.click()

    def check_item_in_basket(self):
        self.check_name_on_page_and_in_basket()
        self.check_price_on_page_and_in_basket()

    def check_name_on_page_and_in_basket(self):
        name1 = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        name2 = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert name1.text == name2.text, "Names of product is differed"

    def check_price_on_page_and_in_basket(self):
        price1 = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)
        price2 = self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert price1.text == price2.text, "Price of products is differed"

    def go_to_basket(self):
        basket_button = self.driver.find_element(*ProductPageLocators.BASKET_LINK)
        basket_button.click()

