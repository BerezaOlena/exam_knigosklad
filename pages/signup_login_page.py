from ..pages import base_page, locators
import inspect


class SignupLoginPage(base_page.BasePage):

    def is_login_signup_push(self):
        assert self.click_element(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button 'login_signup' is not present or intractable"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_login_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_TEXT), \
            "Button 'login_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.LOGIN_PUSH), \
            "Button 'login_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_email_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_EMAIL_TEXT), \
            "Button 'login_email_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_email(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_EMAIL), \
            "Button 'login_email' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_email_input(self, email):
        assert self.input_data(*locators.SignupLoginPageLocators.LOGIN_EMAIL, email), \
            "Button 'login_email_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_password_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_PASSWORD_TEXT), \
            "Button 'login_password_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_password(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN_PASSWORD), \
            "Button 'login_password' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_password_input(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.LOGIN_PASSWORD, password), \
            "Button 'login_password_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_remember_me(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.REMEMBER_ME), \
            "Button 'remember_me' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_button(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LOGIN), \
            "Button 'login_button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_button_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.LOGIN), \
            "Button 'login_button_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_forgot_pass(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.FORGOT_PASS), \
            "Button 'forgot_pass' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_login_successful(self):
        assert self.is_element_appears_after_while(*locators.SignupLoginPageLocators.LOGIN_SUCCESSFUL, timeout=5), \
            "Button 'login_successful' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.SIGNUP), \
            "Button 'signup_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.SIGNUP), \
            "Button 'signup_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_personal_info(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PERSONAL_INFO), \
            "Button 'personal_info' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_firstname_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.FIRSTNAME_TEXT), \
            "Button 'firstname_text(' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_firstname(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.FIRSTNAME), \
            "Button 'firstname' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_firstname_input(self, firstname):
        assert self.input_data(*locators.SignupLoginPageLocators.FIRSTNAME, firstname), \
            "Button 'firstname_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_lastname_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LASTNAME_TEXT), \
            "Button 'lastname_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_lastname(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.LASTNAME), \
            "Button 'lastname' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_lastname_input(self, lastname):
        assert self.input_data(*locators.SignupLoginPageLocators.LASTNAME, lastname), \
            "Button 'lastname_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.EMAIL_TEXT), \
            "Button 'email_text(' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.EMAIL), \
            "Button 'email' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_email_input(self, email):
        assert self.input_data(*locators.SignupLoginPageLocators.EMAIL, email), \
            "Button 'email_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_subscribed_checkbox(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.SUBSCRIBED_CHECKBOX), \
            "Button 'subscribed_checkbox' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_subscribed_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.SUBSCRIBED_TEXT), \
            "Button 'subscribed_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_title(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_TITLE), \
            "Button 'password_title' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_TEXT), \
            "Button 'password_text(' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD), \
            "Button 'password' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_input(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD, password), \
            "Button 'password_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_confirm_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_CONFIRM_TEXT), \
            "Button 'password_confirm_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_confirm(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.PASSWORD_CONFIRM), \
            "Button 'password_confirm' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_password_confirm_input(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.PASSWORD_CONFIRM, password), \
            "Button 'password_confirm_input' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_rememberme_checkbox(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.REMEMBERME_CHECKBOX), \
            "Button 'rememberme_checkbox' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_rememberme_text(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.REMEMBERME_TEXT), \
            "Button 'rememberme_text' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup_button(self):
        assert self.is_element_present(*locators.SignupLoginPageLocators.SIGNUP_BUTTON), \
            "Button 'signup_button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_signup_button_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.SIGNUP_BUTTON), \
            "Button 'signup_button_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_register_successful(self):
        assert self.is_element_appears_after_while(*locators.SignupLoginPageLocators.REGISTER_SUCCESSFUL, timeout=5), \
            "Button 'register_successful' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_close_button_push(self):
        assert self.click_element(*locators.SignupLoginPageLocators.CLOSE_BUTTON), \
            "Button 'close_button_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_user_button_push(self):
        assert self.click_element(*locators.CabinetPageLocators.USER_BUTTON), \
            "Button 'user_button_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_logout_push(self):
        assert self.click_element(*locators.CabinetPageLocators.LOGOUT), \
            "Button 'logout_push' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")
