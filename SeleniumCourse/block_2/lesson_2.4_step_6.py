# тест должен упасть с ошибкой
# с какой именно - это и есть задание урока

from selenium import webdriver
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)

    browser.get('http://suninjuly.github.io/cats.html')

    browser.find_element_by_id("button")
finally:
    browser.quit()