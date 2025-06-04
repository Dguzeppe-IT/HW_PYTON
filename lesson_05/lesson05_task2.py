from selenium import webdriver
from selenium.webdriver.common.by import By


# Пример для Google Chrome
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
