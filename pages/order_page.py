from ..pages import base_page, locators
import inspect
import re


class OrderPage(base_page.BasePage):

    def click_on_category(self):
        assert self.hover_action(*locators.MainPageLocators.POPULAR_CATEGORIES_2), \
            "Element 'click_on_category' is not present or intractable"
        self.explicitly_wait(2)
        assert self.click_element(*locators.MainPageLocators.POPULAR_CATEGORIES_2), \
            "Element 'click_on_category' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_first_product(self):
        self.explicitly_wait(2)
        assert self.hover_action(*locators.OrderPageLocators.FIRST_BOOK), \
            "Element 'add_to_cart_first_product' is not present"
        self.explicitly_wait(2)
        price = self.get_text(*locators.OrderPageLocators.FIRST_BOOK_PRICE)
        price = int(re.sub("[^0-9]", "", price))  # 42
        assert self.click_element(*locators.OrderPageLocators.FIRST_BOOK_TO_CART), \
            "Element 'add_to_cart_first_product' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    def press_btn_close(self):
        self.explicitly_wait(2)
        assert self.click_element(*locators.ProductPageLocators.SUCCESSFUL_CLOSE), \
            "Element 'press_btn_close' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_to_cart_second_product(self):
        assert self.hover_action(*locators.OrderPageLocators.SECOND_BOOK), \
            "Element 'add_to_cart_second_product' is not present"
        self.explicitly_wait(2)
        price = self.get_text(*locators.OrderPageLocators.SECOND_BOOK_PRICE)
        price = int(re.sub("[^0-9]", "", price))  # 42
        assert self.click_element(*locators.OrderPageLocators.SECOND_BOOK_TO_CART), \
            "Element 'add_to_cart_second_product' is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
        if price:
            return price

    def is_button_cart_push(self):
        assert self.hover_action(*locators.BasePageLocators.CART), \
            "Button 'cart' is not present"
        self.explicitly_wait(2)
        assert self.click_element(*locators.OrderPageLocators.TO_ORDER), \
            "Button 'cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def check_total_price_qty(self, price1, price2):
        total_price = self.get_text(*locators.OrderPageLocators.TOTAL_PRICE)
        self.explicitly_wait(2)
        total_price = int(re.sub("[^0-9]", "", total_price))
        print(f"total_prise int: {total_price}")
        total_actual = price1 + price2
        print(f"total_actual int: {total_actual}")
        assert total_actual == total_price, \
            "Total price doesn't match to actual"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_checkout_push(self):
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_BUTTON), \
            "Button 'is_button_checkout_push' is not present or intractable"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def add_notice(self):
        assert self.input_data(*locators.OrderPageLocators.NOTICE, "Sorry Test.."), \
            "Button 'add_notice' is not present"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_checkout(self):
        assert self.click_element(*locators.OrderPageLocators.CHECKOUT_ORDER_BUTTON), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_message_successful(self):
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.MESSAGE_SUCCESSFUL, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_order(self):
        assert self.is_element_present(*locators.OrderPageLocators.ORDER), \
            "Button 'add_notice' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_name_input(self, name):
        assert self.is_element_present(*locators.OrderPageLocators.NAME), \
            "Button 'name_input' is not present"
        assert self.is_element_present(*locators.OrderPageLocators.NAME_INPUT), \
            "Button 'name_input' is not present"
        assert self.input_data(*locators.OrderPageLocators.NAME_INPUT, name), \
            "Button 'name_input' is not present"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_lastname_input(self, name):
        assert self.is_element_present(*locators.OrderPageLocators.LASTNAME), \
            "Button 'lastname_input' is not present"
        assert self.is_element_present(*locators.OrderPageLocators.LASTNAME_INPUT), \
            "Button 'lastname_input' is not present"
        assert self.input_data(*locators.OrderPageLocators.LASTNAME_INPUT, name), \
            "Button 'lastname_input' is not present"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_telephone_input(self, phone):
        assert self.is_element_present(*locators.OrderPageLocators.TELEPHONE), \
            "Button 'telephone' is not present"
        assert self.is_element_present(*locators.OrderPageLocators.TELEPHONE_INPUT), \
            "Button 'telephone_input' is not present"
        assert self.input_data(*locators.OrderPageLocators.TELEPHONE_INPUT, phone), \
            "Button 'telephone_input' is not present"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_city(self):
        assert self.is_element_present(*locators.OrderPageLocators.CITY), \
            "Button 'city' is not present"
        assert self.click_element(*locators.OrderPageLocators.CITY), \
            "Button 'city' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_city_dnipro(self):
        assert self.is_element_present(*locators.OrderPageLocators.CITY_DNIPRO), \
            "Button 'city_dnipro' is not present"
        assert self.click_element(*locators.OrderPageLocators.CITY_DNIPRO), \
            "Button 'city_dnipro' is not present"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_free_shipping(self):
        assert self.is_element_present(*locators.OrderPageLocators.FREE_SHIPPING), \
            "Button 'free_shipping' is not present"
        assert self.click_element(*locators.OrderPageLocators.FREE_SHIPPING), \
            "Button 'free_shipping' is not present"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_payment(self):
        assert self.is_element_present(*locators.OrderPageLocators.PAYMENT), \
            "Button 'payment' is not present"
        assert self.click_element(*locators.OrderPageLocators.PAYMENT), \
            "Button 'payment' is not present"
        self.explicitly_wait(2)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
