import time

import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

# @pytest.mark.parametrize('link', ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                       marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"))
# def test_guest_can_add_product_to_cart(driver, link):
#     productPage = ProductPage(driver, link)
#     productPage.open()
#     productPage.should_be_add_to_basket_btn()
#     productPage.add_item_to_basket()
#     productPage.solve_quiz_and_get_code()
#     productPage.check_item_in_basket()
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    productPage = ProductPage(driver, link)
    productPage.open()
    productPage.should_be_add_to_basket_btn()
    productPage.add_item_to_basket()
    productPage.solve_quiz_and_get_code()
    productPage.check_item_in_basket()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        loginPage = LoginPage(driver, link)
        loginPage.open()
        loginPage.register_new_user()
        loginPage.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        productPage = ProductPage(driver, link)
        productPage.open()
        productPage.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        productPage = ProductPage(driver, link)
        productPage.open()
        productPage.add_item_to_basket()
        productPage.check_item_in_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    productPage = ProductPage(driver, link)
    productPage.open()
    productPage.add_item_to_basket()
    productPage.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    productPage = ProductPage(driver, link)
    productPage.open()
    productPage.add_item_to_basket()
    time.sleep(1)
    productPage.should_be_disappeared()

def test_guest_should_see_login_link_on_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    productPage = ProductPage(driver, link)
    productPage.open()
    productPage.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    productPage = ProductPage(driver, link)
    productPage.open()
    productPage.go_to_basket()
    basketPage = BasketPage(driver, link)
    basketPage.basket_is_empty()