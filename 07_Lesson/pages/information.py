from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Information:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def put_information(self):
        first_name = self.driver.find_element(By.XPATH, '//*[@id="first-name"]')
        first_name.send_keys('Olga')
        last_name = self.driver.find_element(By.XPATH, '//*[@id="last-name"]')
        last_name.send_keys('Ivanova')
        zip_code = self.driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        zip_code.send_keys('140140')
        self.driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    def check_price(self):
        total = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.summary_total_label'))
        ).text
        return total
