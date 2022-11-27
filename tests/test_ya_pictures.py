import pytest
import requests
from selenium.webdriver import Keys
from info_message import Messages
import pages_elements_search


@pytest.mark.usefixtures("setup")
class TestYandexSearch:

    def test_server_response(self):
        response = requests.get("https://yandex.ru")
        if response.status_code == 200:
            print('Запрос выполнен успешно!')
            assert True
        else:
            print('Запрос не завершился успехом!')
            assert False

    def test_yandex_images_search(self):
        iframe_path = self.driver.find_element('xpath', "//*[@class = 'dzen-search-arrow-common__frame']")
        self.driver.switch_to.frame(iframe_path)
        search_field = self.driver.find_element('xpath', '//input[@name="text"]')
        search_field.send_keys("Яндекс картинки")
        search_field.send_keys(Keys.RETURN)

    def test_yandex_images_click(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        yandex_images = self.driver.find_element('xpath', '//a[@accesskey="1" and @href="https://yandex.ru/images/"]')
        yandex_images.click()
        self.driver.switch_to.window(self.driver.window_handles[2])
        images_url = self.driver.current_url
        Messages.check_yandex_images_url(images_url)

    def test_first_theme_click(self):
        first_theme = self.driver.find_element('xpath', '//*[contains(@class, "PopularRequestList-Item_pos_0")]')
        first_theme.click()
        text = self.driver.find_element('xpath', '//*[contains(@class, "Item_pos_0") and @data-grid-text]').text
        input_box = self.driver.find_element('xpath', '//input[@type ="text" and @role = "combobox"]')
        Messages.check_search_field_text(input_box, text)

    def test_click_first_image(self):
        first_image = self.driver.find_element('xpath', '//img[@class = "serp-item__thumb justifier__thumb"]')
        first_image.click()
        assert (self.driver.find_element('xpath', '//img[@class ="MMImage-Origin"]')), 'Изображение не открылось'

    def test_change_image(self):
        src_first_image = self.driver.find_element('xpath', '//img[@class = "MMImage-Origin" and @src]').text
        next_button = self.driver.find_element('xpath', '//*[contains(@class, "CircleButton_type_next")]')
        next_button.click()
        src_second_image = self.driver.find_element('xpath', '//img[@class = "MMImage-Origin" and @src]').text
        assert src_first_image != src_second_image, 'Изображение не поменялось'

    def test_back_image(self):
        src = self.driver.find_element('xpath', '//img[@class = "MMImage-Origin" and @src]').text
        prev_button = self.driver.find_element('xpath', '//*[contains(@class, "CircleButton_type_prev")]')
        prev_button.click()
        src_change = self.driver.find_element('xpath', '//img[@class = "MMImage-Origin" and @src]').text
        assert src != src_change, 'Изображение не поменялось'


    







   


