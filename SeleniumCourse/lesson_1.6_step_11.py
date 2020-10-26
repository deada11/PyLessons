from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_xpath('//input[contains(@class, "first") and @required]').send_keys("Tester")

    browser.find_element_by_xpath('//input[contains(@class, "second") and @required]').send_keys("Pester")

    browser.find_element_by_xpath('//input[contains(@class, "third") and @required]').send_keys("Wester")

    # Использование такой конструкции пропустит баг, т.к.
    # выберет все элементы с тегом required, т.е. 2 штуки,
    # заполнит их данными и нажмет кнопку.
    # Таким образом, пропущенное поле Last Name останется незамеченным
    #
    # elements = browser.find_elements_by_css_selector('input:required')
    # for element in elements:
    #     element.send_keys('test')
    #

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()