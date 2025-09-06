from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FULL), \
           "Your basket is not empty"
        
    def should_be_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
           "Your basket not contain empty message"
        