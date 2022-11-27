from BaseApp import BasePage


class YandexSearchLocators:

    yandex_iframe_path = ('xpath', "//*[@class = 'dzen-search-arrow-common__frame']")
    yandex_search_field = ('xpath', '//input[@name="text"]')


class SearchHelper(BasePage):

    def switch_to_iframe(self):
        iframe = self.find_element(YandexSearchLocators.yandex_iframe_path)
        return self.driver.switch_to.frame(iframe)
    
    # def enter_word(self, word):
    #
    #     search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
    #     search_field.click()
    #     search_field.send_keys(word)
    #     return search_field

    # def click_on_the_search_button(self):
    #     return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()
    #
    # def check_navigation_bar(self):
    #     all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu
    #
    # def check_suggest_field(self):
    #     assert self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_SUGGEST)
    #
    # def assert_results(self, word):
    #     result_field = browser.find_elements_by_css_selector('.path.path_show-https.organic__path > a > b')
    #     url_list = [elem.text.strip() for elem in result_field[:5]]
    #
    #     if word not in url_list:
    #         raise Exception('сайта "Тензор" нет в первых 5 пунктах')



    

