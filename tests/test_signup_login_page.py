import pytest
from ..pages.base_page import BasePage
from ..pages.signup_login_page import SignupLoginPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.signup_login_page
class TestSignupLoginPage:

    def setup_method(self):
        user_name = "%016x" % random.getrandbits(64)
        self.email_for_signup = f"{user_name}@mail.com"
        self.user_name_for_signup = f"{user_name}"
        self.user_name2_for_signup = f"qq{user_name}qq"
        self.password_for_signup = f"@@{user_name}@@"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.MAIN_LINK)
        page.open()

    def test_signup_login_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_login_signup_push()
        page.explicitly_wait(3)
        page.is_login_text()
        page.is_login_email_text()
        page.is_login_email()
        page.is_login_password_text()
        page.is_login_password()
        page.is_remember_me()
        page.is_google_text()
        page.is_login_button()
        page.is_forgot_pass()
        page.is_required_fields()
        page.is_signup()
        page.is_signup_push()
        page.is_personal_info()
        page.is_firstname_text()
        page.is_firstname()
        page.is_lastname_text()
        page.is_lastname()
        page.is_email_text()
        page.is_email()
        page.is_subscribed_checkbox()
        page.is_subscribed_text()
        page.is_password_title()
        page.is_password_text()
        page.is_password()
        page.is_password_confirm_text()
        page.is_password_confirm()
        page.is_rememberme_checkbox()
        page.is_signup_button()
        page.explicitly_wait(2)
        page.is_close_button_push()

    def test_login(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_login_signup_push()
        page.is_login_email_input(sets.TEST_EMAIL)
        page.is_login_password_input(sets.PASSWORD)
        page.explicitly_wait(3)
        page.is_login_button_push()
        page.is_login_successful()
        page.explicitly_wait(3)

    def test_logout(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_user_button_push()
        page.is_logout_push()
        page.is_logout_successful()
        page.explicitly_wait(3)

    def test_signup(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SignupLoginPage(browser, self.link_to_cabinet)
        page.is_login_signup_push()
        page.is_signup_push()
        page.is_firstname_input(self.user_name_for_signup)
        page.is_lastname_input(self.user_name2_for_signup)
        page.is_email_input(self.email_for_signup)
        page.is_password_input(self.password_for_signup)
        page.is_password_confirm_input(self.password_for_signup)
        page.explicitly_wait(3)
        page.is_signup_button_push()
        page.is_register_successful()
        page.explicitly_wait(3)


# pytest -s -v
# -m "signup_login_page"
# --browser_name="firefox"
# --browser_mode="headless"
# --browser_window_size="norma"
