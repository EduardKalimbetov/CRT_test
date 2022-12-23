import time

from selenium.webdriver.common.by import By

def is_element_present(browser,how, what):
    try:
        browser.find_element(how, what)
    except Exception:
        return False
    return True

def test_sung_up_name(browser):

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    button_sing_up.click()

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="name"]')
    input_name.send_keys('Eduard')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert is_element_present(browser, By.CSS_SELECTOR,'[class="notification is-danger"]') != False, 'The test passes registration without a password and email'

def test_sung_up_name_email(browser):

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    button_sing_up.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('Ei@yandex.ru')

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="name"]')
    input_name.send_keys('Eduard')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert is_element_present(browser, By.CSS_SELECTOR,'[class="notification is-danger"]') != False, 'The test passes registration without a password'
def test_sung_up_password(browser):

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    button_sing_up.click()

    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys('123456789')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert is_element_present(browser, By.CSS_SELECTOR,'[class="notification is-danger"]') != False, 'The test passes registration without a email'

def test_sung_up_email_password(browser):

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    button_sing_up.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('a@yandex.ru')

    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys('123456789')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert is_element_present(browser, By.CSS_SELECTOR,'[class="notification is-danger"]') == False, 'Email address already exists. Go to login page.'

def test_sung_up(browser):

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    button_sing_up.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('doxete@yandex.ru')

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="name"]')
    input_name.send_keys('Eduard')

    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys('123456789')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert is_element_present(browser, By.CSS_SELECTOR,'[class="notification is-danger"]') == False, 'Email address already exists. Go to login page.'



