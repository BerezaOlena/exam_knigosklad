import pytest
from ..pages.base_page import BasePage
from ..pages.search_page import SearchPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.search_page
class TestSearchPage:

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.MAIN_LINK)
        page.open()

    def test_search_page(self, browser):
        self.link_to_cabinet = browser.current_url
        page = SearchPage(browser, self.link_to_cabinet)
        page.is_search_book(sets.SEARCH)
        page.is_search_button_push()
        page.is_result()
        page.is_result_right()
        page.is_on_page_search()
        page.is_on_page_button_search()
        page.is_on_page_20_search()
        page.is_on_page_40_search()
        page.is_on_page_80_search()
        page.is_on_page_160_search()
        page.is_sort_button_search()
        page.is_sort_relevant_search()
        page.is_sort_name_search()
        page.is_sort_price_search()
        page.is_sort_new_search()
        page.is_sort_most_viewed_search()
        page.is_sort_text_search()
        page.is_sort_button_search()
        page.is_sort_icon_search()
        page.explicitly_wait(5)


# pytest -s -v
# -m "search_page"
# --browser_name="firefox"
# --browser_mode="headless"
# --browser_window_size="norma"
