﻿link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

def test_add_to_cart(browser):
    page = link   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    page.add_product_to_cart()            # жмем кнопку добавить в корзину 
    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом