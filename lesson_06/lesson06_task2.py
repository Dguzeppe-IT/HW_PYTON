from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

username_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
username_field.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)
