import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def browser(driver="chrome"):
    print("\nstart browser for test ... ")
    if driver == "chrome":
        browser = webdriver.Chrome()
    elif driver == "firefox":
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser ... ")
    browser.quit()
