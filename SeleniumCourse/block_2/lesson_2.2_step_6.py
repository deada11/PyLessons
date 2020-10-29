from selenium import webdriver
import time
import math

def calc(num):
  return str(math.log(abs(12*math.sin(int(num)))))

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/execute_script.html')

    x = int(browser.find_element_by_id('input_value').text)

    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)

    button = browser.find_element_by_class_name('btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element_by_id("robotCheckbox").click()

    browser.find_element_by_id("robotsRule").click()

    button.click()

finally:
    time.sleep(7)
    browser.quit()


