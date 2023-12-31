import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        user_name = "%016x" % random.getrandbits(64)
        self.email_for_subscribe = f"{user_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.MAIN_LINK)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_o_nas()
        page.is_button_payment_delivery()
        page.is_button_contacts()
        page.is_button_language_ukr()
        page.is_button_language_rus()
        page.is_button_search_input()
        page.is_button_search()
        page.is_button_logo_ks()
        page.is_button_contacts1()
        page.is_button_contacts2()
        page.is_button_contacts3()
        page.is_button_callback()
        page.is_button_contacts_icon()
        page.is_button_login_signup_icon()
        page.is_button_login_signup()
        page.is_button_cart_icon()
        page.is_button_cart()
        page.explicitly_wait(3)

    def test_main_page_body(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_left_arrow()
        page.is_right_arrow()
        page.is_button_slide_menu_1()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_2()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_3()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_4()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_5()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_6()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_7()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_8()
        page.is_right_arrow_push()
        page.explicitly_wait(2)
        page.is_button_slide_menu_9()
        # page.is_button_novelty_text() # прибрали з сайта
        page.is_button_novelty_books_3()
        page.is_button_bestsellers_text()
        page.is_button_bestsellers_books_2()
        page.is_button_popular_categories_text()
        page.is_button_popular_categories_2()
        page.is_button_popular_categories_2_text()
        page.is_button_read_together()
        page.explicitly_wait(2)

    def test_main_page_header_scroll(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.scroll_page()
        page.explicitly_wait(2)
        page.is_button_catalog_scrolling()
        page.is_button_catalog_button_scrolling()
        page.is_button_fiction_literature_scrolling()
        page.explicitly_wait(2)
        page.is_button_logo_scrolling()
        page.is_button_search_button_scrolling()
        page.is_button_cart_scrolling()
        page.is_button_cart_count_scrolling()
        page.explicitly_wait(2)

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_logo_ks_mini_footer()
        page.is_button_subscribed_footer()
        page.is_button_subscribed_label_footer()
        page.is_button_subscribed_email_footer()
        page.is_button_subscribed_button_footer()
        page.is_button_o_nas_footer()
        page.is_button_payment_delivery_footer()
        page.is_button_contacts_footer()
        page.is_button_offer_footer()
        page.is_button_policy_footer()
        page.is_button_address_footer()
        # page.is_button_made_in_footer() # прибрали з сайта
        page.explicitly_wait(2)

    def test_main_page_subscribed_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribed_email_footer_input(self.email_for_subscribe)
        page.explicitly_wait(2)
        page.is_button_subscribed_button_footer_push()
        page.explicitly_wait(2)


# pytest -s -v
# -m "main_page"
# --browser_name="firefox"
# --browser_mode="headless"
# --browser_window_size="norma"
