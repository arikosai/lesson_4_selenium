from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def should_be_product_in_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        name_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT)
        assert name.text == name_alert.text, 'Product is not in basket'

    def should_be_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        price_alert = self.browser.find_element(*ProductPageLocators.PRICE_ALERT)
        assert price.text == price_alert.text, 'Prices are not the same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
        
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message did not disappear, but should be"