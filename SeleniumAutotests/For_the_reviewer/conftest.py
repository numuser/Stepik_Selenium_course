import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language: en, ru, ...'
                     )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    option = Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart Chrome browser for test ... ")
    browser = webdriver.Chrome(option=option)
    yield browser

    print("\nquit browser ... ")
    browser.quit()
