import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basket(browser):
    browser.get(link)
    # time.sleep(30) для проверок с различными языками (нужно ревьюеру)
    assert browser.find_element_by_class_name('btn-add-to-basket'), 'There is no button!'
