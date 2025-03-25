import math
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x, y):
    return str(int(x) + int(y))


try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    result_value1 = value1.text

    value2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    result_value2 = value2.text

    sum_result = calc(result_value1, result_value2)
    print(sum_result)


    select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    select.select_by_value(sum_result)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
