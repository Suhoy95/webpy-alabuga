# 202203301225 Разбор 1-го модуля с API

## Задача 1. Разворачивание пакетов с версией по заданию

1. Склонировать себе git репозиторий: `https://gitlab.com/alabuga/firstyearweb/march-ws-1`
2. Развернуть виртуальное окружение согласно requirements.`txt`.
3.Проверка:

![](2022-03-30-12-27-14.png)

## Задача 2: Разворачивание Django-проекта

1. Запулить main (если старая версия)
2. Создать Django-проект с именем `module1`
3. В нем создать Django-приложение с именем `shop`
4. Должны быть файлы как в файле `django_files.txt`
5.Скрипт `check_djangofiles.sh` для проверки:

![](2022-03-30-12-28-18.png)

## Задача 3. Создание Django-проекта

1. Переключаемся на ветку со своей фамилией
2. Удаляем из .gitignore `module1`, и добавляем строки по скриншоту<br>
![](2022-03-30-12-29-40.png)
3. Коммитим ваш Django-проект и отправляем на gitlab


# Задача 4. Сделаем показ Продуктов по `GET /api/products`

> **Каждый шаг не забываем проверять в Postmane!!!!**<br>
> [YouTube](https://youtu.be/IHB5LW4VWG8)

1. Создайте в приложении `shop`, модель `Product` с необходимыми полями
2. Сделайте во view функцию `get_products()`, которая возвращает `JsonResponse`
3. Привяжите ее в `urls.py` по пути `/api/product`
4. Как все будет готово сделать коммит в своей ветке и запушить<br>
![](2022-03-30-12-44-28.png)
![](2022-03-30-12-45-10.png)
![](2022-03-30-12-46-12.png)
![](2022-03-30-12-44-42.png)
![](2022-03-30-12-47-00.png)
![](2022-03-30-12-47-13.png)
![](2022-03-30-12-47-22.png)
![](2022-03-30-12-50-41.png)

## Задача 5. Сделаем Регистрацию по `POST /api/signup`:

> **Каждый шаг не забываем проверять в Postmane!!!!**<br>
> [Youtube](https://youtu.be/S2rPt07WLyE).

1. Сделаем свою модель пользователя, чтобы не привязываться к Django-Аутентификации <br>
![](2022-03-30-15-11-48.png)

2. Сделаем проверку на то, что метод обрабатывает только `POST`. Выключим `CSRF-Validatoin` (В REST API это не требуется):<br>
![](2022-03-30-15-13-00.png)
![](2022-03-30-15-13-22.png)
![](2022-03-30-15-13-12.png)

3. Для возвращения 404 сделаем функцию возвращающую JSON по ТЗ (Для валидации делаем аналогичную функцию):
![](2022-03-30-15-14-07.png)
![](2022-03-30-15-17-59.png)

4. Загрузка тела запроса, как JSON:
![](2022-03-30-15-15-43.png)
![](2022-03-30-15-15-56.png)

5. Валидация
    1. что все обязательные поля не пустые:<br>
    ![](2022-03-30-15-16-34.png)
    2. Что Email соответствует шаблону:<br>
    ![](2022-03-30-15-17-24.png)
    ![](2022-03-30-15-16-58.png)
    3. Что email еще не занят:<br>
    ![](2022-03-30-15-17-46.png)
    4. Что пароль не менее 6-ти символов:<br>
    ![](2022-03-30-15-18-32.png)
6. Генерация токена
    1. Используем `hashlib` стандартную библиотеку Питона: https://docs.python.org/3.7/library/hashlib.html#hash-algorithms<br>
    ![](2022-03-30-15-19-22.png)
    ![](2022-03-30-15-19-33.png)
    2. Создаем токен по текущему времени/Имени пользователя и Паролю<br>
    ![](2022-03-30-15-20-48.png)
    ![](2022-03-30-15-21-07.png)
    ![](2022-03-30-15-21-16.png)
7. Создаем Пользователя в БД (Проверяем в Админке):<br>
![](2022-03-30-15-23-05.png)

## Задача 6. По аналогии с Регистрацией сделать Аутентификацию пользователя.

![](2022-03-31-09-23-46.png)
![](2022-03-31-09-24-01.png)

# Задача 7. POST /api/cart/<product_id> - Добавление товара в корзину

![](2022-03-31-09-24-35.png)
![](2022-03-31-09-24-53.png)
![](2022-03-31-09-25-03.png)
![](2022-03-31-09-25-14.png)
![](2022-03-31-09-25-36.png)

# Задача 8. Просмотр корзины

![](2022-03-31-08-55-38.png)

# Задача 9. Удаление товаров из корзины

![](2022-03-31-08-56-33.png)

![](2022-03-31-08-56-45.png)

# Задача 10. POST/GET /api/cart Оформление и просмотр заказа

![](2022-03-31-08-57-26.png)

![](2022-03-31-08-57-44.png)

![](2022-03-31-08-57-56.png)

![](2022-03-31-08-58-04.png)

# Задача 11. GET /logout Выход

![](2022-03-31-08-58-41.png)

# Задача 12. [admin] POST /api/product Добавление товара в список

![](2022-03-31-08-59-19.png)
![](2022-03-31-08-59-29.png)

# Задача 13. [admin] Удаление и редактирование товара

![](2022-03-31-09-00-11.png)
![](2022-03-31-09-00-26.png)
![](2022-03-31-09-00-36.png)
![](2022-03-31-09-00-45.png)