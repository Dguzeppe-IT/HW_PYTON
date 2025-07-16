import pytest
from selenium import webdriver
from Authorization_page import Auth_page
from Main_page import Main_page
from Cart_page import Cart_page
from Fill_form import Fill_form_page
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование покупки товаров в интернет магазине")
@allure.description("Тест проверяет корректность работы покупки товаров в интернет магазине")
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_webmarket(driver):
    """
    Тест проверяет работу покупки товаров в интернет магазине.
    """
    authorization = Auth_page(driver)

    with allure.step("Открытие страницы авторизации интернет магазина"):
        driver.get("https://www.saucedemo.com/")
    with allure.step("Заполнение строки user-name"):
        authorization.authorization_l("standard_user")
    with allure.step("Заполнение строки last-name"):
        authorization.authorization_p("secret_sauce")
    with allure.step("Нажатие на кнопку login"):
        authorization.click_login()

    main_page = Main_page(driver)

    with allure.step("Добавление товара по названию"):
        main_page.add_product("Sauce Labs Backpack")
    with allure.step("Добавление товара по названию"):
        main_page.add_product("Sauce Labs Bolt T-Shirt")
    with allure.step("Добавление товара по названию"):
        main_page.add_product("Sauce Labs Onesie")
    with allure.step("Открытие страницы корзины интернет магазина"):
        driver.get("https://www.saucedemo.com/cart.html")

    cart_page = Cart_page(driver)
    with allure.step("Нажатие кнопки checkout"):
        cart_page.checkout()

    fill_form = Fill_form_page(driver)
    with allure.step("Заполнение поля first_name"):
        fill_form.first_name_field("Алексей")
    with allure.step("Заполнение поля last_name"):
        fill_form.last_name_field("Пузаков")
    with allure.step("Заполнение поля zip_code"):
        fill_form.zip_code_field("12345")
    with allure.step("Проверка стоимости товаров"):
        fill_form.total_cost()
