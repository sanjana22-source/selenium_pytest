from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # ✅ VERY IMPORTANT
        self.inventory_title=(By.CLASS_NAME, "title")
        self.products=(By.CLASS_NAME, "inventory_item")
        self.product_names=(By.CLASS_NAME, "inventory_item_name")
        self.product_prices=(By.CLASS_NAME, "inventory_item_price")
        self.shopping_cart_badge=(By.CLASS_NAME, "shopping_cart_badge")
        self.shopping_cart_link=(By.CLASS_NAME, "shopping_cart_link")
        self.add_to_cart_buttons=(By.CSS_SELECTOR, ".btn_inventory")
        self.remove_buttons=(By.CSS_SELECTOR, ".btn_secondary")
        self.sort_dropdown=(By.CLASS_NAME, "product_sort_container")



    def get_inventory_title(self):
        return self.find_locator(self.inventory_title).text

    def get_product_count(self):
        return len(self.find_locators(self.products))

    def get_products(self):
        item_details= self.find_locators(self.products)
        return [item_detail.text for item_detail in item_details]

    def get_product_names(self):
        product_names= self.find_locators(self.product_names)
        return [product_name.text for product_name in product_names]

    def get_product_prices(self):
        all_prices = self.find_locators(self.product_prices)
        return [float(price.text.replace("$",""))for price in all_prices]

    def click_add_to_cart(self, product_name):
        items = self.find_locators(self.products)
        for item in items:
            name = item.find_element(*self.product_names).text
            if name == product_name:
                add_button = item.find_element(*self.add_to_cart_buttons)
                add_button.click()
                break


    def find_cart_badge(self):
        return self.find_locator(self.shopping_cart_badge)

    def click_shopping_cart(self):
        self.click(self.shopping_cart_link)

    def click_remove_button(self, product_name):
        items = self.find_locators(self.products)
        for item in items:
            name = item.find_element(*self.product_names).text
            if name == product_name:
                remove_button = item.find_element(*self.remove_buttons)
                remove_button.click()
                break

    def sort_products(self, sort_option):
        select = Select(self.find_locator(self.sort_dropdown))
        select.select_by_visible_text(sort_option)



