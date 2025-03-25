import math
import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'https://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    value1 = browser.find_element(By.CSS_SELECTOR, '#input_value')
    result_value1 = value1.text
    result = calc(result_value1)


    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    browser.execute_script("window.scrollBy(0, 200);", button)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(result)
    button.click()
finally:
    time.sleep(8)
    browser.quit()
