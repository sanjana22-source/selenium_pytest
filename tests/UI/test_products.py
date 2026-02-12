from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.config_reader import get_config


def test_verify_product_count(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    product_count = inventory_page.get_product_count()
    assert product_count == 6, f"Expected 6 products, but found {product_count}"

def test_verify_product_names(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    product_names = inventory_page.get_product_names()
    expected_names = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)"
    ]
    assert product_names == expected_names, f"Expected product names do not match actual names. Expected: {expected_names}, Actual: {product_names}"


def test_verify_price_for_specific_product(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    product_prices = inventory_page.get_product_prices()
    expected_price = 29.99
    actual_price = product_prices[0]  # Assuming the first product is "Sauce Labs Backpack"
    assert actual_price == expected_price, f"Expected price for 'Sauce Labs Backpack' is {expected_price}, but found {actual_price}"


def test_verify_user_clicks_add_to_cart(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    cart_badge = inventory_page.find_locator(inventory_page.shopping_cart_badge)
    assert cart_badge.text== "1", f"Expected shopping cart badge to show '1' after adding 'Sauce Labs Backpack', but found '{cart_badge.text}'"


def test_verify_user_clicks_add_to_cart_and_remove(driver):
    login = LoginPage(driver)
    config = get_config()
    inventory_page = InventoryPage(driver)
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    inventory_page.click_add_to_cart("Sauce Labs Backpack")
    cart_badge = inventory_page.find_cart_badge()
    assert cart_badge.text == "1", f"Expected shopping cart badge to show '1' after adding 'Sauce Labs Backpack', but found '{cart_badge.text}'"
    inventory_page.click_remove_button("Sauce Labs Backpack")
    assert not inventory_page.is_visible(inventory_page.shopping_cart_badge), "Expected shopping cart badge to be removed after removing the product, but it is still visible"
