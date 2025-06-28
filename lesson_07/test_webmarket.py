import pytest
from selenium import webdriver
from Authorization_page import Auth_page
from Main_page import Main_page
from Cart_page import Cart_page
from Fill_form import Fill_form_page


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_webmarket(driver):
    authorization = Auth_page(driver)
    driver.get("https://www.saucedemo.com/")
    authorization.authorization_l("standard_user")
    authorization.authorization_p("secret_sauce")
    authorization.click_login()

    main_page = Main_page(driver)
    main_page.add_product("Sauce Labs Backpack")
    main_page.add_product("Sauce Labs Bolt T-Shirt")
    main_page.add_product("Sauce Labs Onesie")
    driver.get("https://www.saucedemo.com/cart.html")

    cart_page = Cart_page(driver)
    cart_page.checkout()

    fill_form = Fill_form_page(driver)
    fill_form.first_name_field("Алексей")
    fill_form.last_name_field("Пузаков")
    fill_form.zip_code_field("12345")
    fill_form.total_cost()
