import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value1 = browser.find_element(By.CSS_SELECTOR, '#input_value')
    result_value1 = value1.text

    result = calc(result_value1)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    time.sleep(5)
    browser.quit()