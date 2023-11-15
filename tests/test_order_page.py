import pytest
from ..pages.base_page import BasePage
from ..pages.order_page import OrderPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.order_page
class TestOrderPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.MAIN_LINK)
        page.open()

    def test_checkout(self, browser):
        self.link_to_cabinet = browser.current_url
        page = OrderPage(browser, self.link_to_cabinet)
        page.scroll_page2()
        page.click_on_category()
        page.scroll_page()
        global price_1_product
        price_1_product = page.add_to_cart_first_product()
        page.press_btn_close()
        global price_2_product
        price_2_product = page.add_to_cart_second_product()
        page.press_btn_close()
        page.is_button_cart_scrolling_push()
        page.check_total_price_qty(price_1_product, price_2_product)
        page.is_button_checkout_push()
        page.is_order()
        page.is_name_input(sets.TEST_NAME)
        page.is_lastname_input(sets.TEST_LASTNAME)
        page.is_city()
        page.is_city_dnipro()
        page.is_free_shipping()
        page.is_payment()
        page.add_notice()
        page.press_checkout()
        page.is_telephone_input(sets.TEST_PHONE)
        page.press_checkout()
        page.is_message_successful()
        page.explicitly_wait(2)


# pytest -s -v
# -m "order_page"
# --browser_name="firefox"
# --browser_mode="headless"
# --browser_window_size="norma"
