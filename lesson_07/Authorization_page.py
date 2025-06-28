from selenium.webdriver.common.by import By


class Auth_page():

    def __init__(self, driver):
        self.driver = driver

    def authorization_l(self, query):
        # Авторизация как пользователь standard_user
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys(query)
    
    def authorization_p(self, query):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(query)
    
    def click_login(self):
        button_click = self.driver.find_element(By.ID, "login-button")
        button_click.click()