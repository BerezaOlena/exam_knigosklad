import pytest
from ..pages.base_page import BasePage
from ..pages.category_page import CategoryPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.category_page
class TestCategoryPage:

    def test_category_page(self, browser):
        page = BasePage(browser, sets.MAIN_LINK)
        page.open()
        self.link_to_cabinet = browser.current_url
        page = CategoryPage(browser, self.link_to_cabinet)
        page.is_fiction_literature_push()
        page.is_historical_literature()
        page.is_prose()
        page.is_classic()
        page.is_novels()
        page.is_ukrainian()
        page.is_english()
        page.is_prose_push()
        page.is_collection()
        page.is_modern()
        page.is_modern_push()
        page.is_book_2()
        page.is_page_1_category()
        page.is_page_2_category()
        page.is_page_3_category()
        page.is_page_4_category()
        page.is_page_5_category()
        page.is_page_next_category()
        page.is_page_1_category_down()
        page.is_page_2_category_down()
        page.is_page_3_category_down()
        page.is_page_4_category_down()
        page.is_page_5_category_down()
        page.is_page_next_category_down()
        page.is_sort_name()
        page.is_sort_price()
        page.is_sort_new()
        page.is_sort_most_viewed()
        page.is_sort_text()
        page.is_sort_button()
        page.is_sort_icon()
        page.is_article()
        page.is_on_page()
        page.is_on_page_button()
        page.is_on_page_20()
        page.is_on_page_40()
        page.is_on_page_80()
        page.is_on_page_160()

# pytest -s -v -m category_page --browser_mode="gui"
# pytest -s -v

