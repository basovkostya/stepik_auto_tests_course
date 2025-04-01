from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
class TestRegistration():
    def test_open_stepik(self, browser, lesson):
        s = ''
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.implicitly_wait(10)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.navbar__auth_login').click()
        browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('basov04@mail.ru')
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('Kultivator4!')
        browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()
        time.sleep(5)
        answer = math.log(int(time.time()))
        answer_text = browser.find_element(By.CSS_SELECTOR, 'textarea.textarea')
        answer_text.send_keys(str(answer))
        WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))).click()
        time.sleep(3)
        #description_text = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'p.smart-hints__hint'), 'Correct!'))
        description = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
        result = description.text
        if result != "Correct!":
            s += result
        assert result == "Correct!", 'Неверный ответ'
        print(s)