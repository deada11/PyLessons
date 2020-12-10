from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element_by_css_selector('[type="submit"]').click()

    browser.switch_to.window(browser.window_handles[1])

    browser.find_element_by_id('answer').send_keys(str(math.log(math.fabs(12*math.sin(int(browser.find_element_by_id('input_value').text))))))

    browser.find_element_by_class_name('btn-primary').click()
finally:
    time.sleep(1)

    print(browser.switch_to.alert.text.split()[-1])

    browser.quit()