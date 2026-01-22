from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()
button_text = button.text
print(f'("{button_text}")')

driver.quit()
