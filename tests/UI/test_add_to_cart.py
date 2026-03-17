import time

import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.file_reader import get_config

@pytest.mark.ui
def test_verify_product_added_to_cart(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    inventory_page.click_shopping_cart()
    cart_items= cart_page.get_cart_items()
    expected_items = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    assert cart_items == expected_items, f"Expected items in cart: {expected_items}"

@pytest.mark.ui
def test_verify_product_added_to_cart_and_remove(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_shopping_cart()
    cart_page.remove_item_from_cart("Sauce Labs Backpack")
    cart_items= cart_page.get_cart_items()
    expected_items = []
    assert cart_items == expected_items, f"Expected items in cart: {expected_items}"

@pytest.mark.ui
def test_verify_product_added_to_cart_and_remove_multiple_items(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_add_to_cart("Sauce Labs Bike Light")
    inventory_page.click_add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.click_add_to_cart("Sauce Labs Fleece Jacket")
    inventory_page.click_shopping_cart()
    cart_page.remove_item_from_cart("Sauce Labs Backpack")
    cart_page.remove_item_from_cart("Sauce Labs Fleece Jacket")
    cart_items= cart_page.get_cart_items()
    expected_items = ["Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt"]
    assert cart_items == expected_items, f"Expected items in cart: {expected_items}"

@pytest.mark.ui
def test_verify_user_clicks_continue_shopping_after_adding_to_cart(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_shopping_cart()
    cart_page.continue_shopping()
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/inventory.html"
    assert current_url == expected_url, f"Expected to be redirected to inventory page after clicking 'Continue Shopping', but found {current_url}"

@pytest.mark.ui
def test_verify_user_clicks_checkout_after_adding_to_cart(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    inventory_page.click_shopping_cart()
    cart_page.proceed_to_checkout()
    current_url = driver.current_url
    expected_url = "https://www.saucedemo.com/checkout-step-one.html"
    assert current_url == expected_url, f"Expected to be redirected to checkout page after clicking 'Checkout', but found {current_url}"
