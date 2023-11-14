import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..pages.product_page import ProductPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.product_page
class TestProductPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.MAIN_LINK)
        page.open()

    def test_product_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = ProductPage(browser, self.link_to_cabinet)
        page.scroll_page()
        page.explicitly_wait(3)
        page.is_button_bestsellers_books_2_push()
        page.is_book_name()
        page.is_book_availability()
        page.is_book_number()
        page.is_book_price()
        page.is_book_to_cart()
        page.is_book_to_wishlist()
        page.is_book_description()
        page.is_book_description_text()
        page.explicitly_wait(3)

    def test_product_to_cart(self, browser):
        self.link_to_cabinet = browser.current_url
        page = ProductPage(browser, self.link_to_cabinet)
        page.is_book_to_cart_push()
        page.is_to_cart_successful()
        page.explicitly_wait(3)
        page.is_to_cart_successful_close()
        page.explicitly_wait(3)

    def test_product_to_wishlist(self, browser):
        self.link_to_cabinet = browser.current_url
        page = ProductPage(browser, self.link_to_cabinet)
        page_s = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_book_to_wishlist_push()
        page_s.is_login_email_input(sets.TEST_EMAIL)
        page_s.is_login_password_input(sets.PASSWORD)
        page_s.is_login_button_push()
        page.is_to_wishlist_successful()
        page.explicitly_wait(3)
        page.is_add_to_wishlist_successful_close()
        page.explicitly_wait(3)

# pytest -s -v
# -m "product_page"
# --browser_name="firefox"
# --browser_mode="gui"
# --browser_window_size="max"
