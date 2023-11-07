from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    # HEADER
    def is_button_o_nas(self):
        assert self.is_element_present(*locators.BasePageLocators.O_NAS), \
            "Button 'o_nas' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_payment_delivery(self):
        assert self.is_element_present(*locators.BasePageLocators.PAYMENT_DELIVERY), \
            "Button 'payment&delivery' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_contacts(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS), \
            "Button 'contacts' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_language_ukr(self):
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_UKR), \
            "Button 'language_ukr' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_language_rus(self):
        assert self.is_element_present(*locators.BasePageLocators.LANGUAGE_RUS), \
            "Button 'language_rus' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_search_input(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "Button 'search_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_search(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "Button 'search' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_logo_ks(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_KS), \
            "Button 'logo_ks' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_contacts1(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS1), \
            "Button 'contacts1' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_contacts2(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS2), \
            "Button 'contacts2' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_contacts3(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS3), \
            "Button 'contacts3' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_callback(self):
        assert self.is_element_present(*locators.BasePageLocators.CALLBACK), \
            "Button 'callback' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_contacts_icon(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS_ICON), \
            "Button 'contacts_icon' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_login_signup_icon(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP_ICON), \
            "Button 'login_signup_icon' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_login_signup(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button 'login_signup' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_cart_icon(self):
        assert self.is_element_present(*locators.BasePageLocators.CART_ICON), \
            "Button 'cart_icon' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_cart(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "Button 'cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    # BODY
    def is_button_fiction_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.FICTION_LITERATURE), \
            "Button 'fictional_literature' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_historical_literature(self):
        assert self.is_element_present(*locators.MainPageLocators.HISTORICAL_LITERATURE), \
            "Button 'historical_literature' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_historical_novels(self):
        assert self.is_element_present(*locators.MainPageLocators.HISTORICAL_NOVELS), \
            "Button 'historical_novels' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_1(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_1), \
            "Button 'slide_menu_1' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_2(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_2), \
            "Button 'slide_menu_2' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_3(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_3), \
            "Button 'slide_menu_3' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_4(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_4), \
            "Button 'slide_menu_4' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_5(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_5), \
            "Button 'slide_menu_5' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_6(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_6), \
            "Button 'slide_menu_6' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_7(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_7), \
            "Button 'slide_menu_7' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_8(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_8), \
            "Button 'slide_menu_8' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_slide_menu_9(self):
        assert self.is_element_present(*locators.MainPageLocators.SLIDE_MENU_9), \
            "Button 'slide_menu_9' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_novelty_text(self):
        assert self.is_element_present(*locators.MainPageLocators.NOVELTY_TEXT), \
            "Button 'novelty_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_novelty_books_3(self):
        assert self.is_element_present(*locators.MainPageLocators.NOVELTY_BOOKS_3), \
            "Button 'novelty_books_3' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_bestsellers_text(self):
        assert self.is_element_present(*locators.MainPageLocators.BESTSELLERS_TEXT), \
            "Button 'bestsellers_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_bestsellers_books_2(self):
        assert self.is_element_present(*locators.MainPageLocators.BESTSELLERS_BOOKS_2), \
            "Button 'bestsellers_books_2' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_popular_categories_text(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_CATEGORIES_TEXT), \
            "Button 'popular_categories_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_popular_categories_2(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_CATEGORIES_2), \
            "Button 'popular_categories_2' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_popular_categories_2_text(self):
        assert self.is_element_present(*locators.MainPageLocators.POPULAR_CATEGORIES_2_TEXT), \
            "Button 'popular_categories_2_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_read_together(self):
        assert self.is_element_present(*locators.MainPageLocators.READ_TOGETHER), \
            "Button 'read_together' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    # FOOTER
    def is_button_logo_ks_mini_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_KS_MINI_FOOTER), \
            "Button 'logo_ks_mini_footer' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribed_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_FOOTER), \
            "Button 'subscribed_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribed_label_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_LABEL_FOOTER), \
            "Button 'subscribed_label_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribed_email_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_EMAIL_FOOTER), \
            "Button 'subscribed_email_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribed_button_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBED_BUTTON_FOOTER), \
            "Button 'subscribed_button_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_o_nas_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.O_NAS_FOOTER), \
            "Button 'o_nas_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_payment_delivery_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.PAYMENT_DELIVERY_FOOTER), \
            "Button 'payment_delivery_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_contacts_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.CONTACTS_FOOTER), \
            "Button 'contacts_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_offer_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.OFFER_FOOTER), \
            "Button 'offer_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_policy_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.POLICY_FOOTER), \
            "Button 'policy_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_address_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.ADDRESS_FOOTER), \
            "Button 'address_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_made_in_footer(self):
        assert self.is_element_present(*locators.BasePageLocators.MADE_IN_FOOTER), \
            "Button 'made_in_footer' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")


