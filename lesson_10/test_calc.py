import pytest
from selenium import webdriver
from Calculator_page import Calc_page
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    """
    Тест проверяет работу калькулятора.
    """
    with allure.step("Открытие страницы калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    calculator = Calc_page(driver)
    
    with allure.step("Установка задержки 5 секунд"):
        calculator.delay("5")
    with allure.step("Нажатие кнопки 7 на калькуляторе"):
        calculator.click_elment("7")
    with allure.step("Нажатие кнопки + на калькуляторе"):
        calculator.click_elment("+")
    with allure.step("Нажатие кнопки 8 на калькуляторе"):
        calculator.click_elment("8")
    with allure.step("Нажатие кнопки = на калькуляторе"):
        calculator.click_elment("=")
    with allure.step("Ожидание появления результата"):
        calculator.wait_result()
    with allure.step("Возврат текущего результата"):
        result = calculator.get_result()
    with allure.step("Проверка результата"):
        assert result == "15"
