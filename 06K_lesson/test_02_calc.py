import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_calculator():
    # Инициализация драйвера Chrome
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ввод значения 45 в поле с локатором #delay
        delay_field = driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys("45")

        # Нажатие на кнопки калькулятора
        seven_button = driver.find_element(By.XPATH, "//span[text()='7']")
        seven_button.click()

        plus_button = driver.find_element(By.XPATH, "//span[text()='+']")
        plus_button.click()

        eight_button = driver.find_element(By.XPATH, "//span[text()='8']")
        eight_button.click()

        equal_button = driver.find_element(By.XPATH, "//span[text()='=']")
        equal_button.click()

        # Ожидание результата и проверка его значения
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15')
        )
        result = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15"

    finally:
        # Закрытие браузера
        driver.quit()
