from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def should_be_product_in_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT)
        assert name.text == name_alert.text, 'product is not in basket'

    def should_be_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_alert = self.browser.find_element(*ProductPageLocators.PRICE_ALERT)
        assert price.text == price_alert.text, 'prices are not the same'