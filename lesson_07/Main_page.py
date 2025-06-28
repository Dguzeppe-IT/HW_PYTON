from selenium.webdriver.common.by import By


class Main_page():

    def __init__(self, driver):
        self.driver = driver

    def add_product(self, item_name):
        # Добавление товаров в корзину
        add_product = self.driver.find_element(By.XPATH, f"//div[@class='inventory_item']//div[contains(., '{item_name}')]//button")
        add_product.click()

    
    