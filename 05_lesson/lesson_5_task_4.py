from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")
search_username=driver.find_element(By.CSS_SELECTOR, "input[id='username']")
search_username.send_keys("tomsmith")

search_password=driver.find_element(By.CSS_SELECTOR, "input[id='password']")
search_password.send_keys("SuperSecretPassword!")
login_button = driver.find_element(By.CSS_SELECTOR, "i[class='fa fa-2x fa-sign-in']").click()
green_flash=driver.find_element(By.CSS_SELECTOR, "div[id='flash']")
print(green_flash.text)
