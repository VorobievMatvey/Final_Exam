Задание:
-------
Вам необходимо выбрать любой сайт интернет-магазина и написать для него 50-70 автоматизированных тестов с использованием PyTest и Selenium.


Я выбрал сайт интернет-магазина "Строительный двор" (https://www.sdvor.com/)

Файлы:
-----
[test_cart.py](tests/test_cart.py) - содержит автотесты связанные с корзиной товаров

[test_links.py](tests/test_links.py) - содержит автотесты связанные с ссылками

[test_search.py](tests/test_search.py) - содержит автотесты связанные с поиском

[sdvor.py](pages/sdvor.py) - содержит локаторы используемых элементов в автотестах

Команда для запуска тестов:
--------------------------

```bash
python3 -m pytest -v --driver Chrome --driver-path ~/chromedriver tests/*```


 
