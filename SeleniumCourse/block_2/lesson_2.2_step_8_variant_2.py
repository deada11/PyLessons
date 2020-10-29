from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))
try:
    browser.get('http://suninjuly.github.io/file_input.html')

    # elements = browser.find_elements_by_css_selector('.form-control, required')
    # elements = browser.find_elements_by_css_selector('.form-group> input, .form-group ~ input')

    elements = browser.find_elements_by_tag_name('input')

    # можно и так:
    # for element in elements:
    #     if element.get_attribute('placeholder'):
    #         element.send_keys('tester')
    #     elif element.get_attribute('accept'):
    #         element.send_keys(os.path.join(current_dir, 'test.txt'))

    for element in elements:
        if element.get_attribute('type') == 'text':
            element.send_keys('tester')
        else:
            element.send_keys(os.path.join(current_dir, 'test.txt'))

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(7)
    browser.quit()
