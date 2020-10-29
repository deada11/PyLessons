from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))
try:
    browser.get('http://suninjuly.github.io/file_input.html')

    elements = browser.find_elements_by_css_selector('.form-control, required')

    for element in elements:
        element.send_keys('Tester')

    browser.find_element_by_id('file').send_keys(os.path.join(current_dir, 'test.txt'))

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(7)
    browser.quit()