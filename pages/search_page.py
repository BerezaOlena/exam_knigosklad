from ..pages import base_page, locators
import inspect
import re
from ..settings import sets


class SearchPage(base_page.BasePage):

    def is_search_book(self, word):
        self.explicitly_wait(2)
        assert self.input_data(*locators.BasePageLocators.SEARCH_INPUT, word), \
            "Button 'search_book' is not present"
        self.explicitly_wait(1)
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_button_push(self):
        assert self.click_element(*locators.BasePageLocators.SEARCH_BUTTON), \
            "Button 'search_button_push' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_result(self):
        assert self.is_element_present(*locators.SearchPageLocators.RESULT), \
            "Button 'result' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_result_right(self):
        assert self.is_element_present(*locators.SearchPageLocators.RESULT), \
            "Button 'result_right' is not present"
        result = self.get_text(*locators.SearchPageLocators.RESULT)
        print(f"{result}")
        search_word = int(result.find(sets.SEARCH))
        # print(f"{search_word}")
        assert search_word != -1, \
            "Search_word doesn't match to actual"
        self.explicitly_wait(2)
        print(f"{sets.SEARCH} - Ok")

    def is_on_page_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.ON_PAGE_SEARCH), \
            "Button 'on_page_search' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_on_page_button_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.ON_PAGE_BUTTON_SEARCH), \
            "Button 'on_page_button_search' is not present"
        assert self.hover_action(*locators.SearchPageLocators.ON_PAGE_BUTTON_SEARCH), \
            "Button 'on_page_button_search' is not present"
        assert self.click_element(*locators.SearchPageLocators.ON_PAGE_BUTTON_SEARCH), \
            "Button 'on_page_button_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_on_page_20_search(self):
        assert self.hover_action(*locators.SearchPageLocators.ON_PAGE_20_SEARCH), \
            "Button 'on_page_20_search' is not present"
        assert self.is_element_present(*locators.SearchPageLocators.ON_PAGE_20_SEARCH), \
            "Button 'on_page_20_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_on_page_40_search(self):
        assert self.hover_action(*locators.SearchPageLocators.ON_PAGE_40_SEARCH), \
            "Button 'on_page_40_search' is not present"
        assert self.is_element_present(*locators.SearchPageLocators.ON_PAGE_40_SEARCH), \
            "Button 'on_page_40_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_on_page_80_search(self):
        assert self.hover_action(*locators.SearchPageLocators.ON_PAGE_80_SEARCH), \
            "Button 'on_page_80_search' is not present"
        assert self.is_element_present(*locators.SearchPageLocators.ON_PAGE_80_SEARCH), \
            "Button 'on_page_80_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_on_page_160_search(self):
        assert self.hover_action(*locators.SearchPageLocators.ON_PAGE_160_SEARCH), \
            "Button 'on_page_160_search' is not present"
        assert self.is_element_present(*locators.SearchPageLocators.ON_PAGE_160_SEARCH), \
            "Button 'on_page_160_search' is not present"
        assert self.click_element(*locators.SearchPageLocators.ON_PAGE_BUTTON_SEARCH), \
            "Button 'on_page_button_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_button_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_BUTTON_SEARCH), \
            "Button 'sort_button_search' is not present"
        assert self.click_element(*locators.SearchPageLocators.SORT_BUTTON_SEARCH), \
            "Button 'sort_button_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_relevant_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_RELEVANT_SEARCH), \
            "Button 'sort_relevant_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_name_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_NAME_SEARCH), \
            "Button 'sort_name_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_price_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_PRICE_SEARCH), \
            "Button 'sort_price_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_new_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_NEW_SEARCH), \
            "Button 'sort_new_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_most_viewed_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_MOST_VIEWED_SEARCH), \
            "Button 'sort_most_viewed_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_text_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_TEXT_SEARCH), \
            "Button 'sort_text_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_sort_icon_search(self):
        assert self.is_element_present(*locators.SearchPageLocators.SORT_ICON_SEARCH), \
            "Button 'sort_icon_search' is not present"
        assert self.click_element(*locators.SearchPageLocators.SORT_ICON_SEARCH), \
            "Button 'sort_icon_search' is not present"
        self.explicitly_wait(1)
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
