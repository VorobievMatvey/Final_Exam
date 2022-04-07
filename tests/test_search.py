import pytest


from pages.sdvor import MainPage


def test_24_search(web_browser):
    """ Тестирование поиска по слову "котел". """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    all_names = page.products_names.get_text()

    # Проверям, что поиск нашел товары
    assert page.products_names.count() > 0


    # проверяем что нашли то, что искали:
    for name in all_names:
        msg = 'Wrong product in search "{}"'.format(name)
        assert 'котел' in name.lower(), msg


def test_25_wrong_input_search(web_browser):
    """ Тест поиска при вводе на английской раскладке. """

    page = MainPage(web_browser)

    page.search.send_keys('rjntk\n')
    page.wait_page_loaded()
    all_names = page.products_names.get_text()

    # Проверям, что поиск нашел товары
    assert page.products_names.count() > 0

    # проверяем что нашли то, что подразумевали:
    for name in all_names:
        msg = 'Wrong product in search "{}"'.format(name)
        assert 'котел' in name.lower(), msg


@pytest.mark.xfail(reason="Сортировка не обрабатывает продукт, которого нет в наличии")
def test_26_check_sort_by_price_up(web_browser):
    """ Тест сортировки от меньшего к большему """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.listbox.click()
    page.sort.click()
    page.wait_page_loaded()

    # Записываем все цены
    all_prices = page.products_prices.get_text()

    # Конвертируем все в числа
    all_prices = [float(p.replace(' ', '').replace('₽', '')) for p in all_prices]

    # Проверяем, что сортировка работает правильно
    assert all_prices == sorted(all_prices)


@pytest.mark.xfail(reason="Сортировка не обрабатывает продукт, которого нет в наличии")
def test_27_check_sort_by_price_down(web_browser):
    """ Тест сортировки от большего к меньшему """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.listbox.click()
    page.rev_sort.click()
    page.wait_page_loaded()

    # Записываем все цены
    all_prices = page.products_prices.get_text()

    # Конвертируем цены в числа
    all_prices = [float(p.replace(' ', '').replace('₽', '')) for p in all_prices]

    # Разворачиваем отсортированный список
    rev_prices = sorted(all_prices)[::-1]

    # Проверяем, что сортировка работает правильно
    assert all_prices == rev_prices


@pytest.mark.xfail(reason="Сортировка не обрабатывает продукт, которого нет в наличии")
def test_28_check_sort_by_alphabet(web_browser):
    """ Тест сортировки от А до Я """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.listbox.click()
    page.alphabet.click()
    page.wait_page_loaded()

    # Записываем все названия продуктов
    all_names = page.products_names.get_text()

    # Проверяем, что сортировка работает правильно:
    assert all_names == sorted(all_names)


@pytest.mark.xfail(reason="Сортировка не обрабатывает продукт, которого нет в наличии")
def test_29_check_sort_by_rev_alphabet(web_browser):
    """ Тест сортировки от Я до А """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.listbox.click()
    page.rev_alphabet.click()
    page.wait_page_loaded()

    # Записываем все названия продуктов
    all_names = page.products_names.get_text()

    # Разворачиваем отсортированный список
    rev_names = sorted(all_names)[::-1]

    # Проверяем, что сортировка работает правильно:
    assert all_names == rev_names


@pytest.mark.xfail(reason="Продукт не имеет в названии газовый, но является газовым котлом")
def test_30_check_filter_gas_boiler(web_browser):
    """ Тест фильтра "Газовые котлы". """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.gas_boiler.click()
    page.wait_page_loaded()

    # Сохранаяем все названия товаров
    all_names = page.products_names.get_text()

    # Проверям, что поиск нашел товары
    assert page.products_names.count() > 0

    # проверяем что фильтр оставил только газовые котлы:
    for name in all_names:
        msg = 'Wrong product in search "{}"'.format(name)
        assert 'газовый' in name.lower(), msg

@pytest.mark.xfail(reason="Продукт не имеет в названии твердотопливный, но является твердотопливным котлом")
def test_31_check_filter_sf_boiler(web_browser):
    """ Тест фильтра твердотопливных котлов. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.sf_boiler.click()
    page.wait_page_loaded()

    # сохраняем все названия товаров
    all_names = page.products_names.get_text()

    # Проверям, что поиск нашел товары
    assert page.products_names.count() > 0

    # проверяем что фильтр оставил только твердотопливные котлы:
    for name in all_names:
        msg = 'Wrong product in search "{}"'.format(name)
        assert 'твердотопливный' in name.lower(), msg

def test_32_check_filter_sf_boiler_quantity(web_browser):
    """ Проверям кол-во котлов в фильтре твердотопливных котлов. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.sf_boiler.click()
    page.wait_page_loaded()

    # Сохраняем число котлов рядом с фильтром
    quantity = page.sf_boiler_quantity.get_text()
    quantity = int(quantity.replace('(','').replace(')',''))

    # Проверям, что поиск нашел верное количество
    assert page.products_names.count() == quantity


def test_33_check_quantity_double_filter(web_browser):
    """ Проверям кол-во котлов в двойном фильтре. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.sf_boiler.click()
    page.wait_page_loaded()
    page.gas_boiler.click()
    page.wait_page_loaded()

    # Сохраняем кол-во твердотопливных котлов рядом с фильтром
    quantity_sf = page.sf_boiler_quantity.get_text()
    quantity_sf = int(quantity_sf.replace('(','').replace(')',''))

    # Сохраняем кол-во газовых котлов рядом с фильтром
    quantity_gas = page.gas_boiler_quantity.get_text()
    quantity_gas = int(quantity_gas.replace('(', '').replace(')', ''))

    # Сохраняем общее количество котлов при двойном фильтре
    quantity = page.search_quantity.get_text()
    quantity = quantity.replace('(', '').replace(')', '')
    number = []
    for i in quantity.split():
        try:
            number.append(int(i))
        except ValueError:
            pass

    # Проверям, что двойной фильтр объединил кол-во котлов:
    assert number[0] == quantity_sf + quantity_gas


def test_34_reset_filters(web_browser):
    """ Тест сброса фильтров. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    # Сохраняем состояние отсутсвия фильтров
    nofilters = page.search_quantity.get_text()

    page.sf_boiler.click()
    page.wait_page_loaded()

    page.reset_filters.click()
    page.wait_page_loaded()

    # Проверям, что фильтр сбросился
    assert page.search_quantity.get_text() == nofilters


def test_35_reset_search(web_browser):
    """ Тест сброса строки поиска. """

    page = MainPage(web_browser)

    page.search.send_keys('котел')
    page.wait_page_loaded()

    # Проверяем, что поле строки поиска не пустое
    assert page.dirty_searchbox

    page.reset.click()
    page.wait_page_loaded()

    # Проверям, что поле строки поиска пустое
    assert page.clean_searchbox


def test_36_out_of_stock(web_browser):
    """ Тест фильтра "В наличии". """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    # Выбираем фильтр "В наличии"
    page.stock.click()
    page.wait_page_loaded()

    # Проверям, что представлены только те, что в наличии
    assert page.out_of_stock.is_visible() == False


def test_37_check_filter_baxi_quantity(web_browser):
    """ Проверям кол-во котлов в фильтре по бренду Baxi """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.baxi.scroll_to_element()
    page.baxi.click()
    page.wait_page_loaded()

    # Сохраняем число рядом с фильтром Baxi
    quantity = page.baxi_quantity.get_text()
    quantity = int(quantity.replace('(','').replace(')',''))

    # Проверям, что фильтр показывает верное количество
    assert page.products_names.count() == quantity


def test_38_check_images(web_browser):
    """ Проверяем наличие изображения у найденных товаров. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    assert page.images.get_attribute('src') != ''


def test_39_from_price_filter(web_browser):
    """ Тест фильтра продуктов от определенной цены. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    page.price_filter.click()
    page.from_price.is_visible()
    page.from_price.send_keys('200000')
    page.wait_page_loaded()

    # Записываем все цены
    all_prices = page.products_prices.get_text()

    # Конвертируем все в числа
    all_prices = [float(p.replace(' ', '').replace('₽', '')) for p in all_prices]

    # Проверяем, что цена каждого из товаров больше заданной
    for i in range(len(all_prices)):
        assert all_prices[i] >= 200000

def test_40_to_price_filter(web_browser):
    """ Тест фильтра продуктов до определенной цены. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    page.price_filter.click()
    page.to_price.is_visible()
    page.to_price.send_keys('200000')
    page.wait_page_loaded()

    # Записываем все цены
    all_prices = page.products_prices.get_text()

    # Конвертируем все в числа
    all_prices = [float(p.replace(' ', '').replace('₽', '')) for p in all_prices]

    # Проверяем, что цена каждого из товаров меньше заданной
    for i in range(len(all_prices)):
        assert all_prices[i] <= 200000

def test_41_from_to_price_filter(web_browser):
    """ Тест фильтра продуктов от определенной до определенной цены. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    page.price_filter.click()
    page.from_price.is_visible()
    page.from_price.send_keys('100000')

    page.to_price.send_keys('200000')
    page.wait_page_loaded()

    # Записываем все цены
    all_prices = page.products_prices.get_text()

    # Конвертируем все в числа
    all_prices = [float(p.replace(' ', '').replace('₽', '')) for p in all_prices]

    # Проверяем, что цена каждого из товаров в отрезке стоимости
    for i in range(len(all_prices)):
        assert 100000 <= all_prices[i] <= 200000
