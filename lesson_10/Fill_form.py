from selenium.webdriver.common.by import By
import allure


class Fill_form_page():
    @allure.feature("Заполнение формы личными данными")
    def __init__(self, driver):
        """
        Конструктор класса Cart_page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Поиск и заполнение строки first-name")
    def first_name_field(self, first_name):
        """
        Поиск и заполнение строки first-name.

        :param first_name: str - Личные данные Имя.
        """
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys(first_name)

    @allure.step("Поиск и заполнение строки last-name")
    def last_name_field(self, last_name):
        """
        Поиск и заполнение строки last-name.

        :param last_name: str - Личные данные Фамилия.
        """
        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

    @allure.step("Поиск и заполнение строки postal-code и нажатие кнопки continue")
    def zip_code_field(self, zip_code):
        """
        Поиск и заполнение строки postal-code и нажатие кнопки continue.

        :param zip_code: int - Номер карты.
        """
        zip_code_field = self.driver.find_element(By.ID, "postal-code")
        zip_code_field.send_keys(zip_code)

        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()

    @allure.step("Проверка итоговой суммы")
    def total_cost(self):
        """
        Проверка итоговой суммы.
        """
        total_cost = self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        assert total_cost == "Total: $58.29"
