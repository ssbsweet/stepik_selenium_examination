from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    SOMETHING_IN_BASKET = (By.CSS_SELECTOR, ".basket-title")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    REGISTRATION_CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_LOGIN_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")


class MainPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert-success:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".price_color:nth-child(2)")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert-info strong")
