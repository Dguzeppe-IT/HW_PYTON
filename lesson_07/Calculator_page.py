from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc_page():

    def __init__(self, driver):
        self.driver = driver

    def delay(self, value):
        # Ввод значения 45 в поле с локатором #delay
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(value)

    def click_elment(self, button_text):
        # Нажатие на кнопки калькулятора
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def wait_result(self):
        # Ожидание результата 
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

    def get_result(self):
        # сравнение результата
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result.text
