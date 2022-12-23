import time

from selenium.webdriver.common.by import By
from selenium import webdriver

email = 'kp@yandex.ru'
name = 'Eduard'
password = '123456789'


def is_element_present(browser, how, what):
    try:
        browser.find_element(how, what)
    except Exception:
        return False
    return True


def regist(browser):
    global email, name, password

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys(f'{email}')

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="name"]')
    input_name.send_keys(f'{name}')

    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys(f'{password}')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()


def profile(browser):
    global email, password

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys(f'{email}')

    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys(f'{password}')

    button_login_next = browser.find_element(By.TAG_NAME, 'button')
    button_login_next.click()


def test_proverka_url(browser):
    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    button_sing_up.click()

    regist(browser)

    profile(browser)

    assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Welcome')]") != False, 'Error'

    button_home = browser.find_element(By.CSS_SELECTOR, '[href = "/"]')
    button_home.click()

    assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Test')]") != False, 'Error'

    for i in range(10):
        button_login = browser.find_element(By.CSS_SELECTOR, '[href="/profile"]')
        button_login.click()

        assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Welcome')]") != False, 'Error'

        button_home = browser.find_element(By.CSS_SELECTOR, '[href = "/"]')
        button_home.click()

    assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Test')]") != False, 'Error'

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/logout"]')
    button_sing_up.click()

    button_login = browser.find_element(By.CSS_SELECTOR, '[href="/login"]')
    button_login.click()

    assert is_element_present(browser, By.XPATH, "//h3[contains(text(),'Login')]") != False, 'Error'

    browser.execute_script("alert('Test good');")
    time.sleep(5)
    alert = browser.switch_to.alert
    alert.accept()


