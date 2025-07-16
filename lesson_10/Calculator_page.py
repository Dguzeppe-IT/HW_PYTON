from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Calc_page():

    def __init__(self, driver):
        """
        Конструктор класса Calc_page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Установка задержки в секундах")
    def delay(self, value):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.

        :param delay: int — время задержки в секундах.
        """
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(value)

    @allure.step("Нажатие кнопок")
    def click_elment(self, button_text):
        """
        Нажимает на кнопки калькулятора.

        :param button_text: str — текст на кнопке, которую нужно нажать.
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    @allure.step("Ожидание результата ")
    def wait_result(self):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.

        :param delay: int — время задержки в секундах.
        """ 
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
