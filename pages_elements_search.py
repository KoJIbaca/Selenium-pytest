from lib2to3.pgen2 import driver
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser

class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__popup")


class SearchHelper(BasePage):
    
    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_suggest_field(self):
        assert self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_SUGGEST)
    
    def assert_results(self, word):
        result_field = browser.find_elements_by_css_selector('.path.path_show-https.organic__path > a > b')
        url_list = [elem.text.strip() for elem in result_field[:5]]

        if word not in url_list:
            raise Exception('сайта "Тензор" нет в первых 5 пунктах')



    

