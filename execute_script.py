import math
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.CSS_SELECTOR, '#input_value')
    result_value1 = value1.text

    result = calc(result_value1)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script("window.scrollBy(0, 150);", button)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)

    check_value = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check_value.click()

    radio_value = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_value.click()

    button.click()
finally:
    time.sleep(8)
    browser.quit()
