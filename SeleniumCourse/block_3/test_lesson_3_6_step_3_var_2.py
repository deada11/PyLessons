import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

with open("urls.txt", 'r') as file:
    URLs = []
    for url in file:
        url = url.strip('\n')
        URLs.append(url)

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.parametrize('link', URLs)
def test_found_secret_message(browser, link):
    browser.get(f"{link}")
    browser.find_element(By.XPATH, '//textarea').send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name('submit-submission').click()
    text = browser.find_element_by_class_name('smart-hints__hint').text
    assert text == 'Correct!', f"expected {'Correct!'}, but got {text}"
