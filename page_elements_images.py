from lib2to3.pgen2 import driver
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser

class YandexImagesLocators:
    LOCATOR_YANDEX_IMAGES_BUTTON = (By.CSS_SELECTOR, '[data-id="images"]')
    LOCATOR_YANDEX_IMAGES_POPULAR_THEME = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0>.Link")
    LOCATOR_YANDEX_IMAGES_SEARCHFIELD = (By.NAME, "text")
    LOCATOR_YANDEX_IMAGES_FIRST_FOUND_ITEM = (By.CLASS_NAME, "serp-item_pos_0")
    LOCATOR_YANDEX_IMAGES_PAGE_THEME = (By.CLASS_NAME, "Link_theme_normal")
    LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_YANDEX_IMAGES_BUTTON_NEXT = (By.CLASS_NAME, "MediaViewer-ButtonNext")
    LOCATOR_YANDEX_IMAGES_BUTTON_PREV = (By.CLASS_NAME, "MediaViewer-ButtonPrev")


class ImagesNavigation(BasePage):

    def image_visibility(self):
        assert self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_BUTTON)

    def click_on_the_image_button(self):
        return self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_BUTTON, time=2).click()

    def url_image_check(self):        
       assert self.driver.current_url('https://yandex.ru/images/?utm_source=main_stripe_big')

    def open_first_category(self):
        category = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_POPULAR_THEME)
        category_text = category.text
        category.click()
        search_text = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_SEARCHFIELD).get_attribute('value')
        assert category_text == search_text, f"Wrong request text. Expected {category_text}, got {search_text}"

    def open_first_image(self):
        image = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_FIRST_FOUND_ITEM)
        data = self.json_to_dict(self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_FIRST_FOUND_ITEM).get_attribute('data-bem'))
        image_title = self.quote_to_symbol(data['serp-item']['snippet']['title'].strip())
        image.click()
        image_page_theme = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_PAGE_THEME).text
        assert image_title == image_page_theme, f"Wrong page. Expected {image_title}, got {image_page_theme}"

    def click_next(self):
        self.first_image = self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE).get_attribute('src')
        next_button = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_BUTTON_NEXT)
        next_button.click()
        new_image = self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE).get_attribute('src')
        assert self.first_image != new_image, "Image didn't change"

    def click_prev(self):
        prev_button = self.find_element(YandexImagesLocators.LOCATOR_YANDEX_IMAGES_BUTTON_PREV)
        prev_button.click()
        image = self.find_element(
            YandexImagesLocators.LOCATOR_YANDEX_IMAGES_ORIGINAL_IMAGE).get_attribute('src')
        assert image == self.first_image, "Images don't match"