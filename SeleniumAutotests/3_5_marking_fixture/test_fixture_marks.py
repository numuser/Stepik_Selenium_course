import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# Чтобы запустить тест с нужной маркировкой,
# нужно передать в командной строке параметр -m и нужную метку:
#
# pytest -s -v -m smoke test_fixture_marks.py
#
# Запуск в удобночитаемом виде
# pytest -s -v -m smoke test_fixture_marks.py -q --tb=no -p no:warnings


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:

    # pytest -s -v -m "smoke and win10" test_fixture81.py
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_login_link2(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию.
# Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду
#
# pytest -s -v -m "not smoke" test_fixture8.py

