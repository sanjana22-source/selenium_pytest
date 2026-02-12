from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME= (By.ID, "user-name")
    PASSWORD= (By.ID, "password")
    LOGIN_BUTTON= (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.send_text(self.USERNAME, username)
        self.send_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text((By.CSS_SELECTOR, "h3[data-test= 'error']"))

    def click_menu_button(self):
        self.click((By.ID, "react-burger-menu-btn"))

    def click_logout_link(self):
        self.click((By.ID, "logout_sidebar_link"))

