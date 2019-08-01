# Необходимый импорт
from selenium.webdriver.common.by import By

# еречень локаторов под разные страницы

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    BASKET_EMPTY = (By.CSS_SELECTOR, "div > #content_inner > p")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators(object):
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert-success:nth-child(1) strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert-info strong")

class ProductPage209Locators(object):
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert-success:nth-child(1) strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert-info strong")