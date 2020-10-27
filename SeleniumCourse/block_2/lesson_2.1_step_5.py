from selenium import webdriver
import math
import  time

def calc(x_element):
  return str(math.log(abs(12*math.sin(int(x_element)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element_by_id("input_value").text
    # x = x_element.text
    y = calc(x_element)


    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_id("robotCheckbox").click()

    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_class_name("btn").click()


finally:
    time.sleep(10)
    browser.quit()