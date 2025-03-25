import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x, y):
  return str(x+y)

try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    result_value1 = value1.text

    value2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    result_value2 = value2.text

    sum_result = calc(result_value1, result_value2)

    input_calc = browser.find_element(By.CSS_SELECTOR, '#dropdown')
    input_calc.send_keys()

    check_value = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check_value.click()

    radio_value = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio_value.click()

    #people_radio = browser.find_element(By.ID, "peopleRule")
    #people_checked = people_radio.get_attribute("checked")
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
