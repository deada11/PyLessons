import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basker_method_1(browser): # browser передается в тест как параметр
    browser.get(link)
    # time.sleep(30) для проверок с различными языками (нужно ревьюеру)
    assert browser.find_element_by_class_name('btn-add-to-basket'), 'There is no button for add to basket!'
    # ассерт именно такой, потому что функция assert возвращает булево значение; т.е. если элемент
    # не будет найден, вернется False, тест упадет и будет выведено сообщение "There is no button!"
    # да, тут можно заморочиться и использовать конструкцию try-except или try-finally,
    # но я не стал этого делать, т.к. такой проверки на наличие кнопки более чем достаточно.

# ---- Второй метод проверки наличия кнопки добавления в корзину ---
# def test_button_add_to_basket_method_2(browser):
#     browser.get(link)
#     # time.sleep(30) для проверок с различными языками (нужно ревьюеру)
#     button = browser.find_element_by_class_name('btn-add-to-basket')
#     assert button.is_displayed() == True, 'There is no button for add to basket!'
#     # это второй способ ассерта, он чуть более читаемый, но более загроможден лишней переменной,
#     # от которой можно избавиться
