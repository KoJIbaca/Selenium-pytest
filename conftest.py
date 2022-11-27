import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    print("Инициализация дрйвера")
    driver = webdriver.Chrome(executable_path = r"./drivers/chromedriver.exe")
    driver.get("https://yandex.ru")
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
