from .pages.product_page_209 import ProductPage209

def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage209(browser, link)
    page.open()
    page.basket_find_and_click()
    page.check_guest_cant_see_success_message_after_adding_product_to_cart()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage209(browser, link)
    page.open()

def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage209(browser, link)
    page.open()
    page.basket_find_and_click()
    page.check_message_disappeared_after_adding_product_to_cart()