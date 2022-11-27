import pytest
import requests
from info_message import Messages
from selenium.webdriver import Keys
from pages_elements_search import SearchHelper as page


@pytest.mark.usefixtures("setup")
class TestYandexSearch:

    # Проверка стаутс-кода сервера
    def test_server_response(self):
        response = requests.get("https://yandex.ru")
        if response.status_code == 200:
            print('Запрос выполнен успешно!')
            assert True
        else:
            print('Запрос не завершился успехом!')
            assert False

    # Ввод в поисковую строку "Тензор"
    # def test_search_field_text(self):
    #     iframe_path = self.driver.find_element('xpath', "//*[@class = 'dzen-search-arrow-common__frame']")
    #     self.driver.switch_to.frame(iframe_path)
    #     search_field = self.driver.find_element('xpath', '//input[@name="text"]')
    #     search_field.send_keys("Тензор")
    #     Messages.check_search_field_text(search_field, 'Тензор')

    def test_search_field_text(self):
        page.switch_to_iframe(self)
        search_field = self.driver.find_element('xpath', '//input[@name="text"]')
        search_field.send_keys("Тензор")
        Messages.check_search_field_text(search_field, 'Тензор')

    # Проверка появления suggest-меню и выполнение поиска по слову "Тензор"
    def test_visibility_popup_menu(self):
        popup_menu = self.driver.find_element('xpath', "//*[@class='body_search_yes']")
        Messages.dropdown_visibility(popup_menu)
        search = self.driver.find_element('xpath', '//input[@name="text"]')
        search.send_keys(Keys.RETURN)

    # Проверка первой ссылки
    def test_check_first_link(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        service_menu = self.driver.find_element('xpath', '//*[@class= "main__content"]')
        Messages.search_results(service_menu)
        first_link = self.driver.find_element('xpath', "//a[@accesskey='1' and @href='https://tensor.ru/']")
        Messages.check_first_link(first_link)
