from selenium.webdriver.common.by import By


class Add_Items:
    def __init__(self, driver):
        self.driver = driver

    def add_items(self):
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
