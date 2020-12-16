import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# ---- Первый метод проверки наличия кнопки добавления в корзину ----
def test_button_add_to_basker_method_1(browser): # browser передается в тест как параметр
    browser.get(link)
    # time.sleep(30) для проверок с различными языками (нужно ревьюеру)
    assert browser.find_element_by_class_name('btn-add-to-basket'), 'There is no button for add to basket!'
    # достаточно такого ассерта, потому что функция assert получит некий элемент и вернет булево значение; т.е. если
    # элемент не будет найден, assert получит None, тест упадет и будет выведено сообщение "There is no button!"

# ---- Второй метод проверки наличия кнопки добавления в корзину ----
# def test_button_add_to_basker_method_1(browser): # browser передается в тест как параметр
#     browser.get(link)
#     # time.sleep(30) для проверок с различными языками (нужно ревьюеру)
#     assert len(browser.find_element_by_class_name('btn-add-to-basket').text) > 0, \
#         'There is no button for add to basket!'
#     # тут проверяется не только наличие элемента на странице, но и длина его текста
#     # на случай если в кнопке не будет текста вовсе;
#     # но мне не нравится это решение своей топорностью и отходом от задания

# ---- Третий метод проверки наличия кнопки добавления в корзину ----
# def test_button_add_to_basket_method_2(browser):
#     browser.get(link)
#     # time.sleep(30) для проверок с различными языками (нужно ревьюеру)
#     button = browser.find_element_by_class_name('btn-add-to-basket')
#     assert button.is_displayed() == True, 'There is no button for add to basket!'
#     # это третий способ ассерта, он чуть более читаемый, но загроможден лишней переменной,
#     # от которой можно избавиться
