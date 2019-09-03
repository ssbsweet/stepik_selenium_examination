from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_is_empty(self):
        self.basket_element_is_not_present()
        self.basket_text_about_empty_is_present()

    def basket_element_is_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.SOMETHING_IN_BASKET), "Basket is not empty"

    def basket_text_about_empty_is_present(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), "Text about empty is not present"
