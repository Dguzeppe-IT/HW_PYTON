from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")
driver.find_element(By.CSS_SELECTOR, "button.btn.class2.btn-primary.btn-test").click()
