# python3 -m pytest -v --driver Chrome --driver-path ~/chromedriver tests/*

from pages.sdvor import MainPage


def test_01_shops_link(web_browser):
    """ Кнопка "Магазины" ведет на страницу с магазинами. """

    page = MainPage(web_browser)

    page.shops.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/contacts'


def test_02_articles_link(web_browser):
    """ Кнопка "Статьи" ведет на страницу со списком статей. """

    page = MainPage(web_browser)

    page.articles.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/articles'


def test_03_free_delivery_link(web_browser):
    """ Баннер "Бесплатная доставка" ведет на страницу условий бесплатной доставки. """

    page = MainPage(web_browser)

    page.promo_delivery.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/besplatnaya-dostavka-moskva?promo=p2203_06'


def test_04_consruction_mats_link(web_browser):
    """ Кнопка "Строительные материалы" ведет на страницу каталога стройматериалов. """

    page = MainPage(web_browser)

    page.constr_mats.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/category/stroitelnye-materialy-5521'


def test_05_new_link(web_browser):
    """ Кнопка "Новое в ассортименте" ведет на страницу каталога с новинками. """

    page = MainPage(web_browser)

    page.new.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == \
           'https://www.sdvor.com/moscow/category/catalog?query=:relevance:allCategories:catalog:isNovelty:true'


def test_06_season_link(web_browser):
    """ Кнопка "Сезонные товары" ведет на страницу каталога с сезонными товарами. """

    page = MainPage(web_browser)

    page.season.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == \
           'https://www.sdvor.com/moscow/category/catalog?query=:relevance:allCategories:catalog:isSeasonality:true'


def test_07_heating_link(web_browser):
    """ Кнопка "Отопительное оборудование" ведет на страницу каталога с отопительным оборудованием. """

    page = MainPage(web_browser)

    page.heating.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/category/otopitelnoe-oborudovanie-7784'


def test_08_delivery_link(web_browser):
    """ Кнопка "Подробнее о доставке" ведет на страницу с калькулятором доставки. """

    page = MainPage(web_browser)

    page.delivery.scroll_to_element()
    page.delivery.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/free_delivery'


def test_09_about_link(web_browser):
    """ Кнопка "О компании" ведет на страницу "О компании". """

    page = MainPage(web_browser)

    page.about.scroll_to_element()
    page.about.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/about'


def test_10_benefits_link(web_browser):
    """ Кнопка "Наши преимущества" ведет на страницу преимуществ. """

    page = MainPage(web_browser)

    page.benefits.scroll_to_element()
    page.benefits.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/services'


def test_11_terms_link(web_browser):
    """ Кнопка "Условия продажи товаров" ведет на страницу с публичной офертой. """

    page = MainPage(web_browser)

    page.terms.scroll_to_element()
    page.terms.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/public_offer'


def test_12_vk_link(web_browser):
    """ Кнопка VK ведет на страницу группы в VK. """

    page = MainPage(web_browser)

    page.vk.scroll_to_element()
    page.vk.click()
    page.wait_page_loaded()
    page.switch_to_window()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://vk.com/strdvor'


def test_13_return_link(web_browser):
    """ Кнопка "Cтроительный двор" с отличной страницы ведет на главную страницу. """

    page = MainPage(web_browser)

    page.shops.click()
    page.wait_page_loaded()
    page.sdvor.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow'


def test_14_cart_link(web_browser):
    """ Кнопка "Корзины" ведет на страницу корзины. """

    page = MainPage(web_browser)

    page.cart.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/cart'


def test_15_cart_to_catalog_link(web_browser):
    """ Ссылка перехода в каталог из пустой корзины. """

    page = MainPage(web_browser)

    page.cart.click()
    page.wait_page_loaded()
    page.cart_to_catalog.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/category/stroitelnye-materialy-5521'


def test_16_check_cart_link_in_search(web_browser):
    """ Проверяем ссылку перехода в корзину после добавления товара. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.add.click()
    page.go_to_cart.wait_to_be_clickable()
    page.go_to_cart.click()
    page.wait_page_loaded()

    # Проверям, что перешли в корзину
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/cart'

def test_17_buyers_link(web_browser):
    """ Кнопка "Обмен и возврат" в меню ведет на страницу обмена. """

    page = MainPage(web_browser)

    page.buyers.click()
    page.exchange.wait_to_be_clickable()
    page.exchange.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/exchange'


def test_18_close_menu(web_browser):
    """ Тест закрытия меню после повторного нажатия. """

    page = MainPage(web_browser)

    page.buyers.click()
    condition = page.buyers.get_attribute('aria-expanded')
    page.buyers.click()


    # проверяем, что меню убралось
    assert page.buyers.get_attribute('aria-expanded') != condition


def test_19_arrows(web_browser):
    """ Тестировка работы кнопок стрелок. """

    page = MainPage(web_browser)

    page.arrow_right.click()
    page.wait_page_loaded()
    page.arrow_left.click()
    page.wait_page_loaded()

    # Проверяем, что видна кнопка Сезонные товары
    assert page.season.is_visible()


def test_20_metiz_link(web_browser):
    """ Кнопка "Метизы и крепеж" ведет на страницу каталога "Метиз и крепеж". """

    page = MainPage(web_browser)

    page.arrow_right.click()
    page.wait_page_loaded()
    page.metiz.click()
    page.wait_page_loaded()

    # проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/category/metizy-i-krepezh-5674'


def test_21_pagination_link(web_browser):
    """ Тестировка кнопки нумерации страниц. """

    page = MainPage(web_browser)

    page.pagination.click()
    page.wait_page_loaded()

    # Проверяем, что видим раздел Сантехника
    assert page.plumbing.is_visible()


def test_22_roofing_link(web_browser):
    """ Кнопка "Кровельные материалы" в подменю. """

    page = MainPage(web_browser)

    page.catalog.click()
    page.roofing.click()
    page.wait_page_loaded()


    # Проверяем правильная ли ссылка при переходе:
    assert page.get_current_url() == 'https://www.sdvor.com/moscow/category/krovelnye-materialy-9050'


def test_23_open_new_menu(web_browser):
    """ Тест закрытия одного меню при открытии другого меню. """

    page = MainPage(web_browser)

    page.buyers.click()
    condition = page.buyers.get_attribute('aria-expanded')
    page.catalog.click()

    # Проверяем, что меню убралось
    assert page.buyers.get_attribute('aria-expanded') != condition
