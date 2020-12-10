from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    button = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    button.click()

    browser.find_element_by_id('answer').send_keys(
        str(
            math.log(math.fabs(12*math.sin(int(
                browser.find_element_by_id('input_value').text))))))
    browser.find_element_by_id('solve').click()
finally:
    print(browser.switch_to.alert.text.split()[-1])
    browser.quit()