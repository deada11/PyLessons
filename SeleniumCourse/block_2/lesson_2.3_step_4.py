from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

try:
    browser.find_element_by_css_selector('[type="submit"]').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    test = math.log(math.fabs(12*math.sin(int(x))))

    browser.find_element_by_id('answer').send_keys(str(test))

    browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(5)
    browser.switch_to.alert.accept() # это тут просто так
    time.sleep(2)
    browser.quit()