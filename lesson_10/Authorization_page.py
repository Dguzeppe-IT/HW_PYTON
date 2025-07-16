from selenium.webdriver.common.by import By
import allure


class Auth_page():
    @allure.feature("Страница авторизация")
    def __init__(self, driver):
        """
        Конструктор класса Calc_page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Поиск и заполнение строки user-name")
    def authorization_l(self, query):
        """
        Заполнение строки user-name на странице авторизации.

        :param query: str - Логин для авторизации.
        """
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys(query)

    @allure.step("Поиск и заполнение строки password")
    def authorization_p(self, query):
        """
        Заполнение строки password на странице авторизации.

        :param query: int - Пароль для авторизации.
        """
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(query)

    @allure.step("Нажатие на кнопку login")
    def click_login(self):
        """
        Нажатие кнопки login на странице авторизации.
        """
        button_click = self.driver.find_element(By.ID, "login-button")
        button_click.click()
