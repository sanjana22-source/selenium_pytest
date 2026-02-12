from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.items_in_cart = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.remove_buttons = (By.CSS_SELECTOR, ".cart_button")


    def get_cart_items(self):
        items = self.driver.find_elements(*self.items_in_cart)
        return [item.text for item in items]

    def proceed_to_checkout(self):
        self.click(self.checkout_button)

    def continue_shopping(self):
        self.click(self.continue_shopping_button)

    def remove_item_from_cart(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        remove_locator = (By.ID, f"remove-{formatted_name}")
        self.click(remove_locator)

    def is_cart_empty(self):
        try:
            self.find_locator(self.items_in_cart)
            return False
        except:
            return True

    def get_cart_item_count(self):
        items = self.find_locators(self.items_in_cart)
        return len(items)


    def get_cart_item_prices(self):
        items = self.find_locators(self.items_in_cart)
        prices = []
        for item in items:
            price_element = item.find_element(By.CLASS_NAME, "inventory_item_price")
            price_text = price_element.text.replace("$", "")
            prices.append(float(price_text))
        return prices

    def get_cart_item_quantities(self):
        items = self.find_locators(self.items_in_cart)
        quantities = []
        for item in items:
            quantity_element = item.find_element(By.CLASS_NAME, "cart_quantity")
            quantity_text = quantity_element.text
            quantities.append(int(quantity_text))
        return quantities

    def get_cart_total_price(self):
        prices = self.get_cart_item_prices()
        quantities = self.get_cart_item_quantities()
        total_price = sum(price * quantity for price, quantity in zip(prices, quantities))
        return total_price

    def click_checkout(self):
        self.click(self.checkout_button)

