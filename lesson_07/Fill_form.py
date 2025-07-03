from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Fill_form_page():

    def __init__(self, driver):
        self.driver = driver

    def first_name_field(self, first_name):
        # Заполнение формы личными данными
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys(first_name)

    def last_name_field(self, last_name):
        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

    def zip_code_field(self, zip_code):
        zip_code_field = self.driver.find_element(By.ID, "postal-code")
        zip_code_field.send_keys(zip_code)

        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()

    def total_cost(self):
        # Проверка итоговой суммы
        total_cost = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        assert total_cost == "Total: $58.29"
