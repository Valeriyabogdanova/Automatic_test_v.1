from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
put_element = driver.find_element(By.CSS_SELECTOR, "#delay")
put_element.clear()
put_element.send_keys(45)
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

def test_calculator():
    result = WebDriverWait(driver,46).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                              '.screen'), "15"))
    assert result

driver.quit()

