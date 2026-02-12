from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utilities.config_reader import get_config


def test_sorting_products_by_price_low_to_high(driver):
    login = LoginPage(driver)
    config= get_config()
    inventory_page = InventoryPage(driver)
    username= config["credentials"]["valid_username"]
    password= config["credentials"]["valid_password"]
    login.login(username,password)
    inventory_page.sort_products("Price (low to high)")
    product_prices = inventory_page.get_product_prices()
    sorted_prices = sorted(product_prices)
    assert product_prices == sorted_prices, f"Expected products to be sorted by price from low to high, but found {product_prices}"


def test_sorting_products_by_price_high_to_low(driver):
    login = LoginPage(driver)
    config= get_config()
    inventory_page = InventoryPage(driver)
    username= config["credentials"]["valid_username"]
    password= config["credentials"]["valid_password"]
    login.login(username,password)
    inventory_page.sort_products("Price (high to low)")
    product_prices = inventory_page.get_product_prices()
    sorted_prices = sorted(product_prices, reverse=True)
    assert product_prices == sorted_prices, f"Expected products to be sorted by price from high to low, but found {product_prices}"

def test_sorting_products_by_name_a_to_z(driver):
    login = LoginPage(driver)
    config= get_config()
    inventory_page = InventoryPage(driver)
    username= config["credentials"]["valid_username"]
    password= config["credentials"]["valid_password"]
    login.login(username,password)
    inventory_page.sort_products("Name (A to Z)")
    product_names = inventory_page.get_product_names()
    sorted_names = sorted(product_names)
    assert product_names == sorted_names, f"Expected products to be sorted by name from A to Z, but found {product_names}"

def test_sorting_products_by_name_z_to_a(driver):
    login = LoginPage(driver)
    config= get_config()
    inventory_page = InventoryPage(driver)
    username= config["credentials"]["valid_username"]
    password= config["credentials"]["valid_password"]
    login.login(username,password)
    inventory_page.sort_products("Name (Z to A)")
    product_names = inventory_page.get_product_names()
    sorted_names = sorted(product_names, reverse=True)
    assert product_names == sorted_names, f"Expected products to be sorted by name from Z to A, but found {product_names}"
