class PageLinks():
    MAIN_PAGE_URL = "https://selenium1py.pythonanywhere.com/"
    LOGIN_PAGE_URL = "https://selenium1py.pythonanywhere.com/accounts/login/"
    CATALOGUE_URL = "https://selenium1py.pythonanywhere.com/catalogue/"


class BookLinks():
    SHELLCODERS_BOOK_PAGE = "the-shellcoders-handbook_209/"
    CODERS_AT_WORK_BOOK_PAGE = "coders-at-work_207/"


class BookLinksParametrs():
    PROMO_NEWYEAR = "?promo=newYear"
    PROMO_NEWYEAR19 = "?promo=newYear2019"
    PROMO_OFFERS = [f"?promo=offer{i}" for i in range(10)]
