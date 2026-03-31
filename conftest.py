import pytest
from dotenv import load_dotenv
from selenium import webdriver

from pages.home_page import HomePage
from pages.order_page import OrderPage

load_dotenv()


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)