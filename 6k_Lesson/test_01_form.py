from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pkg_resources import iter_entry_points

def test_zip_color():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    zipCodeField = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="zip-code"]')))



    zipCodeField = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="zip-code"]')))
    zipCodeColor = zipCodeField.get_attribute("class")
    assert zipCodeColor == "alert py-2 alert-danger"


    field_names = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]

    for field_name in field_names:
        field = WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.ID, field_name)))
    field_color = field.get_attribute("class")
    assert field_color == "alert py-2 alert-success"

    driver.quit()

