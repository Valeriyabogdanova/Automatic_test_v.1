from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("запуск страницы с калькулятором в браузере")
    def open_calculator(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("установка задержки секунд")
    def put_elements(self):
        """находим поле, в котором проставляются секунды задержки"""
        put_element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        """предварительно очищаем поле на случай, если оно не пустое по дефолту"""
        put_element.clear()
        """устанавливаем требуемое значение времени задержки в секундах"""
        put_element.send_keys(45)

    @allure.step("нажатие на необходимые кнопки с цифрами")
    def put_buttons(self):
        """ нажимается несколько кнопок калькулятора по условию поставленной задачи"""
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()


    @allure.step("получить результат вычисления")
    def check(self):
        """появление результата с использованием условий явного ожидания"""
        result = self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                   '.screen'), "15"))
        """возвращает числовой результат int c экрана калькулятора"""
        return result