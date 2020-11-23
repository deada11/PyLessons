from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    browser.get('https://admin-billing-2.testms.lognex.ru/users')

    browser.find_element_by_name('username').send_keys('admin@lognex')
    browser.find_element_by_name('password').send_keys('lognex')
    browser.find_element_by_css_selector('[value="Войти"]').click()
    browser.find_element_by_css_selector(
        'html body div.l-page vaadin-horizontal-layout vaadin-vertical-layout.l-page-menu vaadin-horizontal-layout vaadin-button')\
        .click()

    time.sleep(1)
    browser.find_element_by_name('username').send_keys(' admin@lognex ')
    browser.find_element_by_name('password').send_keys('lognex')
    browser.find_element_by_css_selector('[value="Войти"]').click()
    browser.find_element_by_css_selector(
        'html body div.l-page vaadin-horizontal-layout vaadin-vertical-layout.l-page-menu vaadin-horizontal-layout vaadin-button')\
        .click()
finally:
    browser.quit()