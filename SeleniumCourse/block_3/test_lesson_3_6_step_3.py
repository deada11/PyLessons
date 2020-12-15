import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('urls.txt', 'r') as file:
    URLs = []
    for url in file:
        url = url.strip('\n')
        URLs.append(url)

class TestFoungSecretMessage():

    @pytest.fixture()
    def ufo_message(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        for url in URLs:
            browser.get(f"{url}")
            browser.find_element(By.XPATH, '//textarea').send_keys(str(math.log(int(time.time()))))
            browser.find_element_by_class_name('submit-submission').click()
            text = browser.find_element_by_class_name('smart-hints__hint').text
            print(text)
        yield text
        browser.quit()

    def test_found_secret_message(self, ufo_message):
        assert ufo_message == 'Correct!',\
            f"expected {'Correct!'}, but got {ufo_message}"
        print(ufo_message)
