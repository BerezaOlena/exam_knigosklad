from ..pages import base_page, locators
import inspect


class ProductPage(base_page.BasePage):

    def is_button_bestsellers_books_2_push(self):
        assert self.hover_action(*locators.MainPageLocators.BESTSELLERS_BOOKS_2), \
            "Button 'bestsellers_books_2_push' is not present"
        self.explicitly_wait(3)
        assert self.click_element(*locators.MainPageLocators.BESTSELLERS_BOOKS_2), \
            "Button 'bestsellers_books_2_push' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_book_name(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_NAME), \
            "Button 'book_name' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_availability(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_AVAILABILITY), \
            "Button 'book_availability' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_number(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_NUMBER), \
            "Button 'book_number' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_price(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_PRICE), \
            "Button 'book_price' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_to_cart(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_TO_CART), \
            "Button 'book_to_cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_to_cart_push(self):
        assert self.click_element(*locators.ProductPageLocators.BOOK_TO_CART), \
            "Button 'book_to_cart_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_to_cart_successful(self):
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.CART_SUCCESSFUL, timeout=7), \
            "Button 'to_cart_successful' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_to_wishlist(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_TO_WISHLIST), \
            "Button 'book_to_wishlist' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_to_wishlist_push(self):
        assert self.click_element(*locators.ProductPageLocators.BOOK_TO_WISHLIST), \
            "Button 'book_to_wishlist_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_to_wishlist_successful(self):
        assert self.is_element_appears_after_while(*locators.OrderPageLocators.CART_SUCCESSFUL, timeout=7), \
            "Button 'to_cart_successful' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_add_to_wishlist_successful_close(self):
        assert self.click_element(*locators.ProductPageLocators.SUCCESSFUL_CLOSE), \
            "Button 'wishlist_successful_close' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_to_cart_successful_close(self):
        assert self.click_element(*locators.ProductPageLocators.SUCCESSFUL_CLOSE), \
            "Button 'wishlist_successful_close' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_description(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_DESCRIPTION), \
            "Button 'book_description' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_book_description_text(self):
        assert self.is_element_present(*locators.ProductPageLocators.BOOK_DESCRIPTION_TEXT), \
            "Button 'book_description_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")
