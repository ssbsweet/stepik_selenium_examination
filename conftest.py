import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose driver: chrome")


@pytest.fixture(scope="function")
def driver(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language}) 
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit driver..")
    driver.quit()
