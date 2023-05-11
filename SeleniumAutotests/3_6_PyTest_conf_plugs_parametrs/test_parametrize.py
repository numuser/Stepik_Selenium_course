import pytest
from selenium.webdriver.common.by import By

# PyTest позволяет запустить один и тот же тест с разными входными параметрами.
# Для этого используется декоратор @pytest.mark.parametrize(). Наш сайт доступен для разных языков.
# Напишем тест, который проверит, что для сайта с русским и английским языком будет отображаться ссылка на форму логина.
# Передадим в наш тест ссылки на русскую и английскую версию главной страницы сайта.

# В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра.

@pytest.mark.parametrize("language", ["ru", "en-gb"])
def test_login_with_languages(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link"
