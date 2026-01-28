from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



class Autorisation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def name_password(self):
        self.driver.get("https://www.saucedemo.com/")
        user = self.driver.find_element(By.ID, "user-name")
        user.clear()
        user.send_keys("standard_user")
        password = self.driver.find_element(By.ID, 'password')
        password.clear()
        password.send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
