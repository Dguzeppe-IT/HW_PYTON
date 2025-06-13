import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




def test_shopping():
    # Инициализация драйвера Firefox
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    try:
        # Открытие сайта магазина
        driver.get("https://www.saucedemo.com/")

        # Авторизация как пользователь standard_user
        username_field = driver.find_element(By.ID, "user-name")
        username_field.send_keys("standard_user")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        password_field.send_keys(Keys.RETURN)

        # Добавление товаров в корзину
        backpack_btn = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Backpack')]]//button")
        backpack_btn.click()

        tshirt_btn = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button")
        tshirt_btn.click()

        onesie_btn = driver.find_element(By.XPATH, "//div[@class='inventory_item' and .//div[contains(text(), 'Sauce Labs Onesie')]]//button")
        onesie_btn.click()

        # Переход в корзину и нажатие Checkout
        cart_btn = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_btn.click()

        checkout_btn = driver.find_element(By.ID, "checkout")
        checkout_btn.click()

        # Заполнение формы личными данными
        first_name_field = driver.find_element(By.ID, "first-name")
        first_name_field.send_keys("Алексей")

        last_name_field = driver.find_element(By.ID, "last-name")
        last_name_field.send_keys("Пузаков")

        zip_code_field = driver.find_element(By.ID, "postal-code")
        zip_code_field.send_keys("12345")

        continue_btn = driver.find_element(By.ID, "continue")
        continue_btn.click()

        # Чтение итоговой стоимости
        total_cost = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

    finally:
        # Закрытие браузера
        driver.quit()

    # Проверка итоговой суммы
    assert total_cost == "Total: $58.29"
