from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/inputs")
search_box = driver.find_element(By.CSS_SELECTOR, "input")
search_box.send_keys("Sky")
driver.find_element(By.CSS_SELECTOR, "input").clear()
search_box = driver.find_element(By.CSS_SELECTOR, "input")
search_box.send_keys("Pro")
driver.quit()
