import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.sdvor.com'

        super().__init__(web_driver, url)

    # Кнопка Магазины
    shops = WebElement(xpath='//a[@href="/moscow/contacts"]')

    # Кнопка Статьи
    articles = WebElement(xpath='//a[@href="/moscow/articles"]')

    # Кнопка Каталог
    catalog = WebElement(class_name='cx-hamburger')

    # Кнопка Кровельные материалы
    roofing = WebElement(xpath='//a[@href="/moscow/category/krovelnye-materialy-9050"]')

    # Баннер Бесплатная доставка
    promo_delivery = WebElement(xpath='//a[@href="/moscow/besplatnaya-dostavka-moskva?promo=p2203_06"]')

    # Кнопка Строительные материалы
    constr_mats = WebElement(xpath='//a[@href="/moscow/category/stroitelnye-materialy-5521"]')

    # Кнопка Новое в ассортименте
    new = WebElement(xpath='//span[@class="name" and contains(text(),"Новое в ассортименте")]')

    # Кнопка Сезонные товары
    season = WebElement(xpath='//span[@class="name" and contains(text(),"Сезонные товары")]')

    # Кнопка Отопительное оборудование
    heating = WebElement(xpath='//span[@class="name" and contains(text(),"Отопительное оборудование")]')

    # Кнопка Метизы и крепеж
    metiz = WebElement(xpath='//span[@class="name" and contains(text(),"Метизы и крепеж")]')

    # Кнопка Сантехника
    plumbing = WebElement(xpath='//span[@class="name" and contains(text(),"Сантехника")]')

    # Кнопка третьей страницы нумерации видов товара
    pagination = WebElement(xpath='//span[@class="swiper-pagination-handle" and @index="2"]')

    # Кнопка стрелки вправо
    arrow_right = WebElement(class_name='swiper-button-next')

    # Кнопка стрелки влево
    arrow_left = WebElement(class_name='swiper-button-prev')

    # Кнопка Подробнее о доставке
    delivery = WebElement(xpath='//a[@class="detail-link" and contains(text(),"Подробнее о доставке")]')

    # Кнопка О компании
    about = WebElement(xpath='//a[@href="/moscow/about" and @class="sub-item"]')

    # Кнопка Покупателям
    buyers = WebElement(xpath='//button[@class="dropdown-toggle nav-item"]')

    # Кнопка Обмен и возврат
    exchange = WebElement(xpath='//a[@href="/moscow/exchange"]')

    # Кнопка Наши преимущества
    benefits = WebElement(xpath='//a[@href="/moscow/services"]')

    # Кнопка Условия продажи товаров
    terms = WebElement(xpath='//a[@class="sub-item" and @href="/moscow/public_offer"]')

    # Кнопка VK
    vk = WebElement(xpath='//img[@alt="Перейти в группу Вконтакте"]')

    # Кнопка Строительный двор для возврата на главную
    sdvor = WebElement(xpath='//a[@role="link" and @href="/moscow"]')

    # Кнопка Корзины
    cart = WebElement(class_name='cart')

    # Переход в каталог из корзины
    cart_to_catalog = WebElement(xpath='//a[@href="/category/stroitelnye-materialy-5521"]')

    # Поле поиска
    search = WebElement(xpath='//input[@placeholder="Поиск"]')

    # Чистое поле поиска
    clean_searchbox = WebElement(class_name='searchbox')

    # Поле поиска с записью
    dirty_searchbox = WebElement(class_name='searchbox dirty')

    # Кнопка очистки строки поиска
    reset = WebElement(xpath='//button[@aria-label="Reset"]')

    # Названия продукции в поиске
    products_names = ManyWebElements(class_name='product-name')

    # Цены продукции в поиске
    products_prices = ManyWebElements(class_name='price')

    # Все изображения найденных товаров
    images = ManyWebElements(xpath='//a[@class="product-image"]//img')

    # Список сортировки
    listbox = WebElement(xpath='//sd-sorting')

    # Сортировка От меньшей к большей
    sort = WebElement(xpath='//span[@class="ng-option-label" and contains(text(), " Цена от меньшей к большей ")]')

    # Сортировка от большей к меньше
    rev_sort = WebElement(xpath='//span[@class="ng-option-label" and contains(text(), " Цена от большей к меньшей ")]')

    # Названия от А до Я
    alphabet = WebElement(xpath='//span[@class="ng-option-label" and contains(text(), " Название от А до Я ")]')

    # Названия от Я до А
    rev_alphabet = WebElement(xpath='//span[@class="ng-option-label" and contains(text(), " Название от Я до А ")]')

    # Фильтр "Газовые котлы"
    gas_boiler = WebElement(xpath='//span[@class="facet-value__name" and contains(text(),"Котлы газовые")]')

    # Фильтр "Котлы твердотопливные"
    sf_boiler = WebElement(xpath='//span[@class="facet-value__name" and contains(text(),"Котлы твердотопливные")]')

    # Кол-во газовых котлов
    gas_boiler_quantity = WebElement(xpath='//span[contains(text(),"Котлы газовые")]/span[@class="facet-value__count"]')

    # Кол-во твердотопливных котлов
    sf_boiler_quantity = WebElement(xpath='//span[contains(text(),"Котлы твердотопливные")]'
                                          '/span[@class="facet-value__count"]')

    # Кол-во товара найденного в поиске
    search_quantity = WebElement(xpath='//h1/span')

    # Кнопка Сбросить фильтры
    reset_filters = WebElement(xpath='//button[@class="btn btn-link active-facets-reset"]')

    # Надпись Нет в наличии
    out_of_stock = WebElement(xpath='//span[@class="d-flex justify-content-center not-available-title"]')

    # Фильтр В наличии
    stock = WebElement(xpath='//span[@class="facet-value__name" and contains(text(),"В наличии")]')

    # Кол-во котлов фирмы Baxi
    baxi_quantity = WebElement(xpath='//span[contains(text(),"Baxi")]/span[@class="facet-value__count"]')

    # Фильтр по бренду Baxi
    baxi = WebElement(xpath='//span[@class="facet-value__name" and contains(text(),"Baxi")]')

    # Добавить в корзину первый найденный продукт
    add = WebElement(xpath='//button[@class="btn btn-gray"]')

    # Кнопка Перейти в корзину после добавления товара в корзину
    go_to_cart = WebElement(xpath='//a[@class="btn btn-go-to-cart"]')

    # Название первого продукта в поиске
    first_name = WebElement(xpath='//a[@class="product-name"]')

    # Название первого продукта в корзине
    first_cartname = WebElement(xpath='//div[@class="cx-name"]/a')

    # Стоимость корзины
    cartcost = WebElement(xpath='//span[@class="total"]')

    # Кнопка "+" у добавленного товара в корзину
    plus = WebElement(xpath='//button[@class="up"]')

    # Кнопка "-" у добавленного товара в корзину
    minus = WebElement(xpath='//button[@class="down"]')

    # Сумма товара в корзине
    sum = WebElement(xpath='//div[@class="info"]/span/span')

    # Цена товаров в корзине
    price = WebElement(xpath='//div[@class="cx-item-list-items"]//div[@class="total"]/div[@class="cx-value"]')

    # Названия товаров в корзине
    cart_products = ManyWebElements(xpath='//div[@class="cx-name"]/a')

    # Кнопка очистить корзину на странице корзины
    clear_cart = WebElement(xpath='//button[@class="btn btn-link remove-btn"]')

    # Пустая корзина
    empty_cart = WebElement(tag_name='h3')

    # Поле количества товара
    amount = WebElement(xpath='//input[@class="withLabel"]')

    # Количество товара в поле
    amount_number = WebElement(xpath='//div[@class="wrapper"]/span[@class="label"]')

    # Фильтр Цена
    price_filter = WebElement(xpath='//button[@class="facet-button" and contains(text(),"Цена")]')

    # Поле ввода цены "От"
    from_price = WebElement(xpath='//input[@formcontrolname="from"]')

    # Поле ввода цены "До"
    to_price = WebElement(xpath='//input[@formcontrolname="to"]')

    # Количество наименований в корзине
    cart_names = WebElement(xpath='//div[@class="cart-icon-block"]/span')
