from selenium import webdriver
import unittest

browser = webdriver.Chrome()

link_1 = 'http://suninjuly.github.io/registration1.html'
link_2 = 'http://suninjuly.github.io/registration2.html'

def found_text(link):
    browser.get(link)
    browser.find_element_by_xpath('//input[contains(@class, "first") and @required]').send_keys("Tester")
    browser.find_element_by_xpath('//input[contains(@class, "second") and @required]').send_keys("Pester")
    browser.find_element_by_xpath('//input[contains(@class, "third") and @required]').send_keys("Wester")

    browser.find_element_by_css_selector("button.btn").click()

    welcome_text_elt = browser.find_element_by_tag_name("h1").text
    browser.quit()
    return welcome_text_elt

class TestLinks(unittest.TestCase):


    def test_link1(self):
        self.assertEqual(found_text(link_1), "Congratulations! You have successfully registered!",
                         "Text should be equal, but not")

    def test_link2(self):
        self.assertEqual(found_text(link_2), "Congratulations! You have successfully registered!",
                         "Text should be equal, but not")

if __name__ == '__main__':
    unittest.main()
