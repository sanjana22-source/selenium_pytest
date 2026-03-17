import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.file_reader import get_config

@pytest.mark.ui
def test_checkout_process(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_shopping_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_information("John", "Doe", "12345")
    checkout_page.click_continue()
    checkout_page.click_finish()
    confirmation_message = checkout_page.get_confirmation_message()
    assert confirmation_message == "Thank you for your order!", f"Expected confirmation message to be 'Thank you for your order!', but found {confirmation_message}"


@pytest.mark.ui
def test_checkout_process_with_missing_information(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_shopping_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_information("", "Doe", "12345")  # Missing first name
    checkout_page.click_continue()
    error_message = checkout_page.get_error_message()
    assert error_message == "Error: First Name is required", f"Expected error message to be 'Error: First Name is required', but found {error_message}"

@pytest.mark.ui
def test_checkout_page_navigation(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_shopping_cart()
    cart_page.click_checkout()
    checkout_page.click_cancel()
    assert 'cart' in driver.current_url, f"Expected to be navigated back to cart page, but current URL is {driver.current_url}"



@pytest.mark.ui
def test_total_price_calculation_on_checkout_page(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    inventory_page.click_shopping_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_information("Sanjana", "amrutansu", "12345")
    checkout_page.click_continue()
    item_total = checkout_page.get_item_total()
    tax = checkout_page.get_tax()
    total_price = checkout_page.get_total_price()
    expected_total_price = item_total + tax
    assert total_price == expected_total_price, f"Expected total price to be {expected_total_price}, but found {total_price}"