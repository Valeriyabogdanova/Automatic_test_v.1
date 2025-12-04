import pytest
import allure
from selenium import webdriver
from class_calculator import Calculator


@pytest.fixture
def driver():
    """
        Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("тестирование Калькулятора")
@allure.description("тест проверяет корректрность работы калькулятора посредством проверки результата сложения")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    calculator = Calculator(driver)
    with allure.step("Открытие страницы калькулятора"):
        calculator.open_calculator()
    with allure.step("Нажатие кнопок"):
        calculator.put_elements()
    calculator.put_buttons()
    with allure.step("Ожидание результата"):
        result = calculator.check()
    with allure.step("Проверка результата"):
        assert result