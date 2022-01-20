from pages_elements_search import SearchHelper
from page_elements_images import ImagesNavigation
from page_elements_images import YandexImagesLocators

def test_yandex_image(browser):
    ya_page = ImagesNavigation(browser)
    ya_page.go_to_site()
    ya_page.image_visibility()
    ya_page.click_on_the_image_button()
    #ya_page.url_image_check()   
    ya_page.open_first_category()
    ya_page.open_first_image()
    ya_page.click_next()
    ya_page.click_prev()
    







   


