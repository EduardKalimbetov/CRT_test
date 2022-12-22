import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('link',['http://localhost:5000/'])
def test_sung_up_name(browser, link):

    browser.get(f'{link}')

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_sing_up)
    button_sing_up.click()

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="name"]')
    input_name.send_keys('Eduard')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert browser.find_element(By.CSS_SELECTOR,'[class="notification is-danger"]') == True,'Good test falls'

@pytest.mark.parametrize('link', ['http://localhost:5000/'])
def test_sung_up_name_email(browser,link):
    browser.get(f'{link}')

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_sing_up)
    button_sing_up.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('E@yandex.ru')

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="name"]')
    input_name.send_keys('Eduard')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert browser.find_element(By.TAG_NAME, 'h3') == 'trye', 'Test proxodit dalche'

@pytest.mark.parametrize('link', ['http://localhost:5000/'])
def test_sung_up_email_password(browser,link):

    browser.get(f'{link}')

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_sing_up)
    button_sing_up.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('a@yandex.ru')

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_name.send_keys('123456789')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert browser.find_element(By.TAG_NAME, 'h3') != 'trye', 'Test ne vipolnil uslovie'

@pytest.mark.parametrize('link',['http://localhost:5000/'])
def test_sung_up_password(browser,link):

    browser.get(f'{link}')

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_sing_up)
    button_sing_up.click()

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_name.send_keys('123456789')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert browser.find_element(By.CSS_SELECTOR, '[class="notification is-danger"]') == True, 'Good test falls'

@pytest.mark.parametrize('link',['http://localhost:5000/'])
def test_sung_up(browser, link):
    browser.get(f'{link}')

    button_sing_up = browser.find_element(By.CSS_SELECTOR, '[href="/signup"]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button_sing_up)
    button_sing_up.click()

    input_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input_email.send_keys('d@yandex.ru')

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="name"]')
    input_name.send_keys('Eduard')

    input_name = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    input_name.send_keys('123456789')

    button_sing_up2 = browser.find_element(By.TAG_NAME, 'button')
    button_sing_up2.click()

    assert browser.find_element(By.TAG_NAME, 'h3') != 'trye', 'Test ne vipolnil uslovie'



