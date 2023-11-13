from ..pages import base_page, locators
import inspect


class CategoryPage(base_page.BasePage):

    def is_fiction_literature_push(self):
        assert self.click_element(*locators.MainPageLocators.FICTION_LITERATURE), \
            "Button 'fiction_literature_push' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_historical_literature(self):
        assert self.is_element_present(*locators.CategoryPageLocators.HISTORICAL_LITERATURE), \
            "Button 'historical_literature' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_prose(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PROSE), \
            "Button 'prose' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_prose_push(self):
        assert self.click_element(*locators.CategoryPageLocators.PROSE), \
            "Button 'prose_push' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_classic(self):
        assert self.is_element_present(*locators.CategoryPageLocators.CLASSIC), \
            "Button 'classic' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_novels(self):
        assert self.is_element_present(*locators.CategoryPageLocators.NOVELS), \
            "Button 'novels' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_ukrainian(self):
        assert self.is_element_present(*locators.CategoryPageLocators.UKRAINIAN), \
            "Button 'ukrainian' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_english(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ENGLISH), \
            "Button 'english' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_collection(self):
        assert self.is_element_present(*locators.CategoryPageLocators.COLLECTION), \
            "Button 'collection' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_modern(self):
        assert self.is_element_present(*locators.CategoryPageLocators.MODERN), \
            "Button 'modern' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_modern_push(self):
        assert self.click_element(*locators.CategoryPageLocators.MODERN), \
            "Button 'modern_push' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_book_2(self):
        assert self.is_element_present(*locators.CategoryPageLocators.BOOK_2), \
            "Button 'book_2' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_1_category(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_1_CATEGORY), \
            "Button 'page_1_category' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_2_category(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_2_CATEGORY), \
            "Button 'page_2_category' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_3_category(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_3_CATEGORY), \
            "Button 'page_3_category' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_4_category(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_4_CATEGORY), \
            "Button 'page_4_category' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_5_category(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_5_CATEGORY), \
            "Button 'page_5_category' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_next_category(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_NEXT_CATEGORY), \
            "Button 'page_next_category' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_1_category_down(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_1_CATEGORY_DOWN), \
            "Button 'page_1_category_down' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_2_category_down(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_2_CATEGORY_DOWN), \
            "Button 'page_2_category_down' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_3_category_down(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_3_CATEGORY_DOWN), \
            "Button 'page_3_category_down' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_4_category_down(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_4_CATEGORY_DOWN), \
            "Button 'page_4_category_down' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_5_category_down(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_5_CATEGORY_DOWN), \
            "Button 'page_5_category_down' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_page_next_category_down(self):
        assert self.is_element_present(*locators.CategoryPageLocators.PAGE_NEXT_CATEGORY_DOWN), \
            "Button 'page_next_category_down' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_sort_name(self):
        assert self.is_element_present(*locators.CategoryPageLocators.SORT_NAME), \
            "Button 'sort_name' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_sort_price(self):
        assert self.is_element_present(*locators.CategoryPageLocators.SORT_PRICE), \
            "Button 'page_sort_price' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_sort_new(self):
        assert self.is_element_present(*locators.CategoryPageLocators.SORT_NEW), \
            "Button 'sort_new' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_sort_most_viewed(self):
        assert self.is_element_present(*locators.CategoryPageLocators.SORT_MOST_VIEWED), \
            "Button 'sort_most_viewed' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_sort_text(self):
        assert self.is_element_present(*locators.CategoryPageLocators.SORT_TEXT), \
            "Button 'sort_text' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_sort_button(self):
        assert self.is_element_present(*locators.CategoryPageLocators.SORT_BUTTON), \
            "Button 'sort_button' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_sort_icon(self):
        assert self.is_element_present(*locators.CategoryPageLocators.SORT_ICON), \
            "Button 'sort_icon' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_article(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ARTICLE), \
            "Button 'article' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_on_page(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ON_PAGE), \
            "Button 'on_page' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_on_page_button(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ON_PAGE_BUTTON), \
            "Button 'on_page_button' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_on_page_20(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ON_PAGE_20), \
            "Button 'on_page_20' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_on_page_40(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ON_PAGE_40), \
            "Button 'on_page_40' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_on_page_80(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ON_PAGE_80), \
            "Button 'on_page_80' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")

    def is_on_page_160(self):
        assert self.is_element_present(*locators.CategoryPageLocators.ON_PAGE_160), \
            "Button 'on_page_160' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - OK")
