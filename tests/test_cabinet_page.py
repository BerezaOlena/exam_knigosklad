import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..pages.cabinet_page import CabinetPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cabinet_page
class TestCabinetPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.MAIN_LINK)
        page.open()

    def test_cabinet_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page_s = SignupLoginPage(browser, self.link_to_cabinet)
        page = CabinetPage(browser, self.link_to_cabinet)
        page_s.is_login_signup_push()
        page.explicitly_wait(2)
        page_s.is_login_email_input(sets.TEST_EMAIL)
        page_s.is_login_password_input(sets.PASSWORD)
        page_s.is_login_button_push()
        page.explicitly_wait(2)
        page.is_user_button()
        page_s.is_user_button_push()
        page.explicitly_wait(2)
        page.is_link_account()
        page.is_link_wishlist()
        page.is_link_checkout()
        page.is_logout()
        page.is_link_account_push()
        page.explicitly_wait(2)
        page.is_title_account()
        page.is_welcome_text()
        page.is_account_info()
        page.is_contact_info()
        page.is_info_letter()
        page.is_address()
        page.is_default_payment()
        page.is_default_address()
        page.is_my_account()
        page.is_info()
        page.is_info_account()
        page.is_address_book()
        page.is_subscribed_news()
        page.is_my_reviews()
        page.is_my_orders()
        page.explicitly_wait(2)

# pytest -s -v
# -m "cabinet_page"
# --browser_name="firefox"
# --browser_mode="headless"
# --browser_window_size="norma"
