from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")
search_place=driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_place.send_keys("Sky")
search_place.send_keys(Keys.RETURN)
search_place.clear()
search_place=driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_place.send_keys("Pro")
search_place.send_keys(Keys.RETURNgi)
driver.quit()
