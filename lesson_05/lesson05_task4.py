from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/login")
username_field = driver.find_element(By.CSS_SELECTOR, "#username")
username_field.send_keys("tomsmith")
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.send_keys("SuperSecretPassword!")
button = driver.find_element(By.CSS_SELECTOR, "#login > button").click()
text_box = driver.find_element(By.CSS_SELECTOR, "#flash")
print(text_box.text)
driver.quit()
