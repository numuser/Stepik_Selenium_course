# Flags:
# -v --tb=line
from .pages.login_page import LoginPage
from .pages.links import PageLinks


def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, PageLinks.LOGIN_PAGE_URL)
    page.open()  # открываем страницу
    page.should_be_login_url()  # выполняем метод страницы — проверяем ссылку на страницу логина


def test_should_see_login_from(browser):
    page = LoginPage(browser, PageLinks.LOGIN_PAGE_URL)
    page.open()  # открываем страницу
    page.should_be_login_form()


def test_should_see_register_from(browser):
    page = LoginPage(browser, PageLinks.LOGIN_PAGE_URL)
    page.open()  # открываем страницу
    page.should_be_register_form()
