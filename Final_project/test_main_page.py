# Flags:
# -v --tb=line --language=en
from .pages.main_page import MainPage

link = "https://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина


def test_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()  # выполняем метод страницы — проверяем видимость кнопки логина
