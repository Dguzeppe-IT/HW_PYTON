from selenium.webdriver.common.by import By
import allure


class Main_page():
    @allure.feature("Добавление товара в корзину по названию товара")
    def __init__(self, driver):
        """
        Конструктор класса Main_page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление товара в корзину")
    def add_product(self, item_name):
        """
        Добавление товаров в корзину по названию товара.

        :param item_name: str - Название товара.
        """
        add_product = self.driver.find_element(By.XPATH, f"//div[@class='inventory_item']//div[contains(., '{item_name}')]//button")
        add_product.click()
