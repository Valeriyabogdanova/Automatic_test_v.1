import pytest
from selenium import webdriver
import allure
from class_autorisation import Autorisation
from class_add_items import Add_Items
from class_chekout import Checkout
from class_information import Information


@pytest.fixture
def driver():
    """
           Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("тестирование магазина одежды")
@allure.description("в данном тестировании проводится комплексная оценка корректной работы интернет-магазина одежды,"
                    "содержащая в себе пошаговые проверки авторизации, выбора одежды из каталога, "
                    "добавления товаров в корзину, заполнение полей личных данных зазазчика "
                    "и соответствие итоговой стоимости товаров сумме, указанной в корзине")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Интернет-магазин")
def test_shop(driver):
    with allure.step("Открытие страницы интернет-магазина"):
        autorisation = Autorisation(driver)
    with allure.step("авторизация (ввесли логин и пароль)"):
        autorisation.name_password()
    with allure.step("Добавить товары в корзину"):
        add_new_items = Add_Items(driver)
    add_new_items.add_items()
    with allure.step("Проверить содержимое корзины"):
        check = Checkout(driver)
    check.checkout()
    with allure.step("Ввести данные заказчика в соответствующие поля"):
        information = Information(driver)
    information.put_information()
    with allure.step("проверить итоговую стоимость товаров в корзине"):
        total = information.check_price()
    with allure.step("убедиться, что стоимоть товаров в корзине равна итоговой стоимости, указанной в поле Total"):
        assert total == "Total: $58.29"