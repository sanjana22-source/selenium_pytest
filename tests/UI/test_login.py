from pages.login_page import LoginPage
from utilities.config_reader import get_config


def test_login_valid_credentials(driver):
    login = LoginPage(driver)
    config = get_config()
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    assert 'inventory' in driver.current_url


def test_login_invalid_credentials(driver):
    login = LoginPage(driver)
    config = get_config()
    username = config["credentials"]["invalid_username"]
    password = config["credentials"]["invalid_password"]
    login.login(username, password)
    error_message = login.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"


def test_login_locked_out_user(driver):
    login = LoginPage(driver)
    config = get_config()
    username = config["credentials"]["locked_username"]
    password = config["credentials"]["locked_password"]
    login.login(username, password)
    error_message = login.get_error_message()
    assert error_message == "Epic sadface: Sorry, this user has been locked out."

def test_verify_logout_functionality(driver):
    login = LoginPage(driver)
    config = get_config()
    username = config["credentials"]["valid_username"]
    password = config["credentials"]["valid_password"]
    login.login(username, password)
    assert 'inventory' in driver.current_url
    login.click_menu_button()
    login.click_logout_link()
    assert 'https://www.saucedemo.com/' in driver.current_url
