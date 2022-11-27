from selenium.common import NoSuchElementException


class Messages:

    def check_search_field_text (path, keyword):
        if path.get_attribute('value') == keyword:
            print (f'Слово {keyword} введено в поле поиска')
            assert True
        else:
            print('Произошла ошибка при вводе')
            assert False

    def dropdown_visibility(path):
        if path.is_displayed() is True:
            print("Выпадающее меню отображается")
            assert True
        else:
            print("Выпадающее меню не отображается")
            assert False

    def search_results(path):
        if path.is_displayed():
            print ("Поисковый запрос выполнен успешно")
            assert True
        else:
            print("Поисковый запрос невыполнен")
            assert False

    def check_first_link(path):
        try:
            path
        except NoSuchElementException:
            print("Первая ссылка не является ссылкой на сайт компании Тензор")
            return False
        print("Первая ссылка ведет на сайт компании Тензор")
        return True

    def check_yandex_images_url(url):
        if url == "https://yandex.ru/images/":
            print ("Яндекс картинки открылись")
            assert True
        else:
            print("Переход на Яндекс-картинки не выполнен")
            assert False





