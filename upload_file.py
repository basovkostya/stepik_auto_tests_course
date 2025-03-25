import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    link = 'https://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("Kostya")
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("Basov")
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("Kostya@mail.ru")
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()