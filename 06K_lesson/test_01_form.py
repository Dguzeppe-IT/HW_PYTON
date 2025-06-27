import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def test_form():
    # Выберите нужный браузер (Edge или Safari)
    driver = webdriver.Edge()  # Для Edge
    # driver = webdriver.Safari()  # Для Safari

    try:
        # Откройте страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        # Заполните форму
        first_name = driver.find_element(By.NAME, "first-name")
        first_name.send_keys("Иван")

        last_name = driver.find_element(By.NAME, "last-name")
        last_name.send_keys("Петров")

        address = driver.find_element(By.NAME, "address")
        address.send_keys("Ленина, 55-3")

        email = driver.find_element(By.NAME, "e-mail")
        email.send_keys("test@skypro.com")

        phone_number = driver.find_element(By.NAME, "phone")
        phone_number.send_keys("+7985899998787")

        # Поле Zip code оставляем пустым

        city = driver.find_element(By.NAME, "city")
        city.send_keys("Москва")

        country = driver.find_element(By.NAME, "country")
        country.send_keys("Россия")

        job_position = driver.find_element(By.NAME, "job-position")
        job_position.send_keys("QA")

        company = driver.find_element(By.NAME, "company")
        company.send_keys("SkyPro")

        # Нажмите кнопку Submit
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Дождитесь обновления страницы
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "zip-code")))

        # Проверьте, что поле Zip code подсвечено красным
        zip_code = driver.find_element(By.ID, "zip-code").get_attribute("class")
        assert zip_code == "alert py-2 alert-danger"

        # Проверьте, что остальные поля подсвечены зеленым
        poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
        for pole in poles:
            pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
            assert pole_class == "alert py-2 alert-success"
    finally:
        # Закройте браузер
        driver.quit()
