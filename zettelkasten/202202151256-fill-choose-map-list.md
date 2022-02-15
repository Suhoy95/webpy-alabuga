# 202202151256 TODO: Заполнение экрана Выбора Карт

Продолжаем разбираться в этапе [Получения Информации о картах Игры](202202151147-fetch-maps-Module-2-WS.md).

На прошлом этапе мы [получили maps.json](202202151200-fetch-maps-json-module2-ws.md),
сейчас нам нужно отобразить информацию о картах на странице в виде карточек.

## Находим верстку карточки

1. Рассмотрим `index.html` и найдем HTML-код одной карточки, а также найдем
какую информацию нам нужно туда подставить. В нашем случае, это картинка (`src`)
и название карты (в нескольких местах):

![](2022-02-15-13-37-22.png)

2. В HTML-коде карточки есть часть непонятных атрибутов, которые нам вроде как
и не нужны. Верстальщик спешил и просто копировал верстку с BootStrap-а.
Поэтому мы можем пока убрать её:

![](2022-02-15-13-54-16.png)

3. На самом деле, мы убрали HTML-аттрибуты для работы с модальным окном
в BootStrap. Мы его будем [делать по-другому](202202151356-login-form-Module-2.md),
но и с [модальными окнами BootStrap](202202151358-modal-window-wth-Bootstrap.md)
было бы неплохо разобраться.

## Создаем функцию по генерации HTML-кода одной карточки

1. Возьмем

![](2022-02-15-14-07-18.png)

2.

3.
![](2022-02-15-14-08-42.png)

4.

![](2022-02-15-14-15-44.png)

5.

![](2022-02-15-14-09-19.png)

6. Не забываем проверить, что ничего не сломалось и все работает также

## Генерирование списка HTML-карточек

1.

![](2022-02-15-14-19-44.png)

2.

![](2022-02-15-14-20-19.png)

3.

![](2022-02-15-14-26-09.png)

4. Не забываем проверить, что ничего не сломалось и все работает также


## Размещение списка HTML-карточек на Экране Выбора Карт

1.

![](2022-02-15-14-22-41.png)

2.

![](2022-02-15-14-23-54.png)

3.

![](2022-02-15-14-24-16.png)

4.

![](2022-02-15-14-25-02.png)

5.

![](2022-02-15-14-26-27.png)



## Следующие шаги

1. Отлично, теперь можно переходить к разработке [выбора экрана](202202151333-change-screen.md)