from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    # n1 = browser.find_element_by_id('num1').text
    # n2 = browser.find_element_by_id('num2').text
    # value = n1 + n2

    value = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)

    selector = Select(browser.find_element_by_id('dropdown'))
    selector.select_by_value(str(value))

    browser.find_element_by_class_name('btn').click()

finally:
    time.sleep(4)
    browser.quit()