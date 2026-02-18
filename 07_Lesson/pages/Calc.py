from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open_calculator(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def put_elements(self):
        put_element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        put_element.clear()
        put_element.send_keys(45)

    def put_buttons(self):
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def check(self):
        result = self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                   '.screen'), "15"))
        return result
