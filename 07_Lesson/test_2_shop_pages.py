import pytest
from selenium import webdriver
from pages.autoriz import Autorisation
from pages.add_items import Add_Items
from pages.checkout import Checkout
from pages.information import Information


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    autorisation = Autorisation(driver)
    autorisation.name_password()
    add_new_items = Add_Items(driver)
    add_new_items.add_items()
    check = Checkout(driver)
    check.checkout()
    information = Information(driver)
    information.put_information()
    total = information.check_price()
    assert total == "Total: $58.29"
