from pages_elements_search import SearchHelper

def test_yandex_search(browser):
    ya_page = SearchHelper(browser)
    ya_page.go_to_site()
    ya_page.enter_word('Тензор')
    ya_page.check_suggest_field()
    ya_page.click_on_the_search_button()
    ya_page.assert_results('Тензор')
