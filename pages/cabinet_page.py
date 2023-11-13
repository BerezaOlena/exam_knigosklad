from ..pages import base_page, locators
import inspect


class CabinetPage(base_page.BasePage):
    def is_user_button(self):
        assert self.is_element_present(*locators.CabinetPageLocators.USER_BUTTON), \
            "Button 'user_button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_link_account(self):
        assert self.is_element_present(*locators.CabinetPageLocators.LINK_ACCOUNT), \
            "Button 'link_account' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_link_account_push(self):
        assert self.click_element(*locators.CabinetPageLocators.LINK_ACCOUNT), \
            "Button 'link_account_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_link_wishlist(self):
        assert self.is_element_present(*locators.CabinetPageLocators.LINK_WISHLIST), \
            "Button 'link_wishlist' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_link_checkout(self):
        assert self.is_element_present(*locators.CabinetPageLocators.LINK_CHECKOUT), \
            "Button 'link_checkout' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_logout(self):
        assert self.is_element_present(*locators.CabinetPageLocators.LOGOUT), \
            "Button 'logout' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_title_account(self):
        assert self.is_element_present(*locators.CabinetPageLocators.TITLE_ACCOUNT), \
            "Button 'title_account' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_welcome_text(self):
        assert self.is_element_present(*locators.CabinetPageLocators.WELCOME_TEXT), \
            "Button 'welcome_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_account_info(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ACCOUNT_INFO), \
            "Button 'account_info' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_contact_info(self):
        assert self.is_element_present(*locators.CabinetPageLocators.CONTACT_INFO), \
            "Button 'contact_info' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_letter(self):
        assert self.is_element_present(*locators.CabinetPageLocators.INFO_LETTER), \
            "Button 'info_letter' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_address(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ADDRESS), \
            "Button 'address' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_default_payment(self):
        assert self.is_element_present(*locators.CabinetPageLocators.DEFAULT_PAYMENT), \
            "Button 'default_payment' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_default_address(self):
        assert self.is_element_present(*locators.CabinetPageLocators.DEFAULT_ADDRESS), \
            "Button 'default_address' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_my_account(self):
        assert self.is_element_present(*locators.CabinetPageLocators.MY_ACCOUNT), \
            "Button 'my_account' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info(self):
        assert self.is_element_present(*locators.CabinetPageLocators.INFO), \
            "Button 'info' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_account(self):
        assert self.is_element_present(*locators.CabinetPageLocators.INFO_ACCOUNT), \
            "Button 'info_account' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_address_book(self):
        assert self.is_element_present(*locators.CabinetPageLocators.ADDRESS_BOOK), \
            "Button 'address_book' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_subscribed_news(self):
        assert self.is_element_present(*locators.CabinetPageLocators.SUBSCRIBED_NEWS), \
            "Button 'subscribed_news' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_my_reviews(self):
        assert self.is_element_present(*locators.CabinetPageLocators.MY_REVIEWS), \
            "Button 'my_reviews' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_my_orders(self):
        assert self.is_element_present(*locators.CabinetPageLocators.MY_ORDERS), \
            "Button 'my_orders' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")
