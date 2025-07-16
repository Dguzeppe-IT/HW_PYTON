from selenium.webdriver.common.by import By
import allure


class Cart_page():

    def __init__(self, driver):
        """
        Конструктор класса Cart_page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие кнопки checkout")
    def checkout(self):
        """
        Поиск и нажатие кнопки checkout.
        """
        checkout_btn = self.driver.find_element(By.ID, "checkout")
        checkout_btn.click()
