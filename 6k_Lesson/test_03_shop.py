from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_total():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 20)
    user = driver.find_element(By.ID, "user-name")
    user.clear()
    user.send_keys("standard_user")
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    wait
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    wait
    first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    first_name.send_keys('Olga')
    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    last_name.send_keys('Ivanova')
    zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    zip_code.send_keys('140140')
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    total = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR,'.summary_total_label'))
                                            ).text
    print(total)

    assert total == "Total: $58.29"

    driver.quit()





