import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FoxService
from selenium.webdriver.firefox.options import Options as FoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox"
                     )
    parser.addoption('--page_language',
                     action='store',
                     default='en',
                     help="Choose language: en, ru, ..."
                     )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("page_language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart Chrome browser for test ... ")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    elif browser_name == "firefox":
        options = FoxOptions()
        options.set_preference('intl.accept_languages', user_language)
        print("\nstart Firefox browser for test ... ")
        browser = webdriver.Firefox(service=FoxService(GeckoDriverManager().install()), options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser ... ")
    browser.quit()
