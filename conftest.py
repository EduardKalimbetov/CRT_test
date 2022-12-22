import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox"
                     )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == 'chrome':
        print('\nStart Chrom browser for test..')
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)

    elif browser_name == 'firefox':
        print('\nStart FireFox browser for test..')
        browser = webdriver.Firefox()
        browser.set_window_size(1920, 1080)
    else:
        raise pytest.UsageError("--browser_name should be Chrome or FireFox")
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()