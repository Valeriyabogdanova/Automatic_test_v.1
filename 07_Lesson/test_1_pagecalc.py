import pytest
from selenium import webdriver
from pages.Calc import Calculator


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calculator = Calculator(driver)
    calculator.open_calculator()
    calculator.put_elements()
    calculator.put_buttons()
    result = calculator.check()
    assert result
