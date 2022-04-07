import pytest
import time

from pages.sdvor import MainPage


def test_42_check_adding_to_cart(web_browser):
    """ Тест добавления продукта в корзину. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    # Сохраняем название первого продукта
    name = page.first_name.get_text()

    page.add.click()

    # Переходим в корзину
    page.go_to_cart.wait_to_be_clickable()
    page.go_to_cart.click()
    page.wait_page_loaded()

    # Проверям, что в корзине тот же товар
    assert page.first_cartname.get_text() == name


def test_43_check_cartcost(web_browser):
    """ Тест расчета стоимости корзины. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    # Сохраняем цену первого продукта
    all_prices = page.products_prices.get_text()
    price = all_prices[0]

    # Добавляем продукт в корзину
    page.add.click()
    page.wait_page_loaded()


    # Проверям, что стоимость у значка корзины равна стоимости товара
    assert page.cartcost.get_text() == price


def test_44_check_many_products_cartcost(web_browser):
    """ Тест расчета стоимости корзины множественного количества товара. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.add.click()
    page.plus.wait_to_be_clickable()
    page.plus.click()
    page.plus.click()
    page.wait_page_loaded()

    # Сохраняем сумму нескольких первых продуктов
    cost = page.sum.get_text()

    # Переходим в корзину
    page.go_to_cart.wait_to_be_clickable()
    page.go_to_cart.click()
    page.wait_page_loaded()


    # Проверям, что стоимость корзины равна стоимости товаров
    assert page.price.get_text() == cost


def test_45_add_two_product(web_browser):
    """ Тест добавления двух товаров. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    # Добавляем первый продукт
    page.add.click()
    time.sleep(2)

    # Добавляем второй продукт
    page.add.click()

    # Переходим в корзину
    page.go_to_cart.wait_to_be_clickable()
    page.go_to_cart.click()
    page.wait_page_loaded()

    # Проверяем, что товаров в корзине два
    assert page.cart_products.count() == 2


def test_46_clear_cart(web_browser):
    """ Тест очистки корзины. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.add.click()

    # Переходим в корзину
    page.go_to_cart.wait_to_be_clickable()
    page.go_to_cart.click()
    page.wait_page_loaded()

    # Очищаем корзину
    page.clear_cart.click()
    page.wait_page_loaded()

    # Убеждаемся, что корзина пуста
    assert 'Ваша корзина пуста.' in page.empty_cart.get_text()


def test_47_change_quantity_by_keys(web_browser):
    """ Тест изменения кол-ва товара через ввод. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()
    page.add.click()
    page.sum.is_visible()

    # Сохраняем цену товара
    one = page.sum.get_text()
    # Конвертируем цену в число
    one = [float(one.replace(' ', '').replace('₽', '')) for p in one]

    # Вписываем число
    page.amount.send_keys('4')

    # Переходим в корзину
    page.go_to_cart.wait_to_be_clickable()
    page.go_to_cart.click()
    page.wait_page_loaded()

    # Сохраняем стоимость 4 товаров
    four = page.price.get_text()
    # Конвертируем цену в число
    four = [float(four.replace(' ', '').replace('₽', '')) for p in four]

    # Убеждаемся, что стоимость верна
    assert four[0] == one[0]*4


def test_48_check_delist_product(web_browser):
    """ Тест удаления товара через кнопку "-". """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    page.add.click()
    page.minus.wait_to_be_clickable()
    page.minus.click()
    page.wait_page_loaded()

    # Проверяем, что кнопки минуса не видно
    assert page.minus.is_visible() == False


def test_49_check_limit_of_product(web_browser):
    """ Тест ограничения на количество добавляемого товара. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    page.add.click()

    # Сохраняем максимально доступное кол-во товара
    maximum = page.amount.get_attribute('max')

    # Вписываем число большее максимального
    page.amount.send_keys('10')
    page.wait_page_loaded()
    page.refresh()

    # Сохраняем количество товара
    quantity = page.amount_number.get_text()
    number = []
    for i in quantity.split():
        try:
            number.append(int(i))
        except ValueError:
            pass

    # Проверяем, что добавилось максимальное количество разрешенного товара
    assert number[0] == int(maximum)


def test_50_cart_number(web_browser):
    """ Тест отображения кол-ва наименований на значке корзины. """

    page = MainPage(web_browser)

    page.search.send_keys('котел\n')
    page.wait_page_loaded()

    # Добавляем первый продукт
    page.add.click()
    time.sleep(2)

    # Добавляем второй продукт
    page.add.click()

    # Переходим в корзину
    page.go_to_cart.wait_to_be_clickable()
    page.go_to_cart.click()
    page.wait_page_loaded()

    # Проверяем, что количество товаров совпадает
    assert page.cart_products.count() == int(page.cart_names.get_text())
