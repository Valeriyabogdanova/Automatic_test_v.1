from selenium.webdriver.common.by import By
import allure


class Add_Items:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("добавить выбранные товары в корзину")
    def add_items(self):
        """
        путем клика на иконку необходимого товара, позиции добавляются в корзину
        :return:
        """
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()