import pytest
from selenium import webdriver
from Calculator_page import Calc_page


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calc(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator = Calc_page(driver)
    calculator.delay("5")
    calculator.click_elment("7")
    calculator.click_elment("+")
    calculator.click_elment("8")
    calculator.click_elment("=")
    calculator.wait_result()
    result = calculator.get_result()
    assert result == "15"
