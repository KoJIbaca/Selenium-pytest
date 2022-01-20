import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import gettext
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path = "G:/Documents/Курсы/Projects/ya(pytest)/drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

def url_visit():
    driver.get("https://yandex.ru")
    return driver.title()

def search_field_visibility ():    
    try:
        driver.find_element_by_xpath('//*[@id="text"]')
    except NoSuchElementException:
        return False
    return True

def search_field_text ():
    driver.find_element_by_xpath('//*[@id="text"]').send_keys('Тензор')
    assert(driver.find_element_by_xpath('//*[@id="text"]').gettext.contains("Тензор")) == True    

def check_suggest_field():
    locator = (By.CSS_SELECTOR, 'body > div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')     
    elements = WebDriverWait(driver).until(EC.visibility_of_element_located(locator))
    assert elements

def seacrh_click():
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div/div[2]/fwap/fwap/fdpprt/div/div/div[1]/div[2]/form/div[2]/button').click()

def assert_results():
    result_field = driver.find_elements_by_css_selector('body > div.main.serp.i-bem > div.main__center > div.main__content > div.content.content_has-branding-first.i-bem > div.content__left.content__left_has-branding-first')
    url_list = [elem.text.strip() for elem in result_field[:5]]

    if "Тензор" not in url_list:
        raise Exception('сайта "Тензор" нет в первых 5 пунктах')

driver.close()
driver.quit()