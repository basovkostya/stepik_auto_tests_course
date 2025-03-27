from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestSite(unittest.TestCase):
    def test_first(self):
        try:
            link = "https://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
            first_name.send_keys('Kostya')

            last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
            last_name.send_keys('Basov')

            email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
            email.send_keys('Kostya@mail.ru')

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Первый тест не сработал")

        finally:
            time.sleep(4)
            browser.quit()

    def test_last(self):
        try:
            link = "https://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]')
            first_name.send_keys('Kostya')

            last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
            last_name.send_keys('Basov')

            email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
            email.send_keys('Kostya@mail.ru')

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered1", welcome_text, "Второй тест не сработал")

        finally:
            time.sleep(4)
            browser.quit()


if __name__ == '__main__':
    unittest.main()
