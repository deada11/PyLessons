from selenium import webdriver
import math
import  time

def calc(num):
  return str(math.log(abs(12*math.sin(int(num)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()

    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_class_name("btn").click()


finally:
    time.sleep(9)
    browser.quit()