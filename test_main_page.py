import pytest

from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.mark.xfail
    def test_guest_can_go_to_login_page(self, driver):
        link = "http://selenium1py.pythonanywhere.com/"
        mainPage = MainPage(driver, link)
        mainPage.open()
        mainPage.go_to_login_page()
        loginPage = LoginPage(driver, link)
        loginPage.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        link = "http://selenium1py.pythonanywhere.com/"
        mainPage = MainPage(driver, link)
        mainPage.open()
        mainPage.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = "http://selenium1py.pythonanywhere.com"
    mainPage = MainPage(driver, link)
    mainPage.open()
    mainPage.go_to_basket()
    basketPage = BasketPage(driver, link)
    basketPage.basket_is_empty()
