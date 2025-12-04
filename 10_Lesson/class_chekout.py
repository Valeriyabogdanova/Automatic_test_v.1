import allure
from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("проверка содержимого корзины")
    def checkout(self):
        self.driver.find_element(By.XPATH, '//*[@id="checkout"]').click()