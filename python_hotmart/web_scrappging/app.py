from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://localhost:8000/#/exemplo/1")


list_of_inputs = driver.find_elements(By.TAG_NAME, "input")

for value in list_of_inputs:
    print(value.get_property("value"))


elements = driver.find_element(
    By.CSS_SELECTOR, '#social[name="user-social-media"]'
).find_elements(By.TAG_NAME, "span")

for social in elements:
    print(social.text)
