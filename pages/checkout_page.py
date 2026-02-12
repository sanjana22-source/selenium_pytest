from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
        self.cancel_button = (By.ID, "cancel")
        self.finish_button = (By.ID, "finish")
        self.checkout_overview_title = (By.CLASS_NAME, "title")
        self.checkout_items = (By.CLASS_NAME, "cart_item")
        self.checkout_item_names = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_item_prices = (By.CLASS_NAME, "inventory_item_price")
        self.checkout_item_quantities = (By.CLASS_NAME, "cart_quantity")
        self.checkout_total_price = (By.CLASS_NAME, "summary_total_label")


    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.send_text(self.first_name_input, first_name)
        self.send_text(self.last_name_input, last_name)
        self.send_text(self.postal_code_input, postal_code)

    def click_continue(self):
        self.click(self.continue_button)


    def get_checkout_details(self):
        items = self.find_locators(self.checkout_items)
        item_details = []
        for item in items:
            name = item.find_element(*self.checkout_item_names).text
            price = item.find_element(*self.checkout_item_prices).text
            quantity = item.find_element(*self.checkout_item_quantities).text
            item_details.append({"name": name, "price": price, "quantity": quantity})
        return item_details

    def get_total_price(self):
        total_text = self.get_text(self.checkout_total_price)
        return float(total_text.replace("Total: $", ""))

    def click_finish(self):
        self.click(self.finish_button)

    def get_confirmation_message(self):
        return self.get_text((By.CLASS_NAME, "complete-header"))

    def get_error_message(self):
        return self.get_text(self.error_message)

    def click_cancel(self):
        self.click(self.cancel_button)

    def get_item_total(self):
        total_text = self.get_text((By.CLASS_NAME, "summary_subtotal_label"))
        return float(total_text.replace("Item total: $", ""))

    def get_tax(self):
        tax_text = self.get_text((By.CLASS_NAME, "summary_tax_label"))
        return float(tax_text.replace("Tax: $", ""))








