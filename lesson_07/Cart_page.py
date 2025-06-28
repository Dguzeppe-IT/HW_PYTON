from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page():

    def __init__(self, driver):
        self.driver = driver
    
    def checkout(self):
        # нажатие Checkout
        checkout_btn = self.driver.find_element(By.ID, "checkout")
        checkout_btn.click()