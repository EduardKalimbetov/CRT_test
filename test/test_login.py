from selenium.webdriver.common.by import By

def is_element_present(browser,how, what):
    try:
        browser.find_element(how, what)
    except Exception:
        return False
    return True

def test_login_entrance(browser):

    button_login = browser.find_element(By.CSS_SELECTOR, '[href="/login"]')
    button_login.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('a@yandex.ru')

    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys('123456789')

    button_login_next = browser.find_element(By.TAG_NAME, 'button')
    button_login_next.click()

    assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Welcome')]") != False, 'Data entry error'

def test_login_entrance_zero_values(browser):
    button_login = browser.find_element(By.CSS_SELECTOR, '[href="/login"]')
    button_login.click()

    button_login_next = browser.find_element(By.TAG_NAME, 'button')
    button_login_next.click()

    assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Welcome')]") == False, 'the input was made with empty data'

def test_login_of_password(browser):

    button_login = browser.find_element(By.CSS_SELECTOR, '[href="/login"]')
    button_login.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('a@yandex.ru')

    button_login_next = browser.find_element(By.TAG_NAME, 'button')
    button_login_next.click()

    assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Welcome')]") == False, 'the input was made with empty data'

def test_login_of_email(browser):

    button_login = browser.find_element(By.CSS_SELECTOR, '[href="/login"]')
    button_login.click()

    input_password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_password.send_keys('123456789')

    button_login_next = browser.find_element(By.TAG_NAME, 'button')
    button_login_next.click()

    assert is_element_present(browser, By.XPATH, "//h1[contains(text(),'Welcome')]") == False, 'the input was made with empty data'