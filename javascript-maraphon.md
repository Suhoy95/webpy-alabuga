# Марафон изучения JavaScript

## День первый - Знакомство с JS. Работа с отладчиком

Всем, привет. С сегодняшнего дня, мы будем читать каждый день learn.javascript.ru.
Пожалуйста, находите 30-40 минут чтобы почитать и понять как работает JavaScript
и работа с HTML-документом в браузере.

Если вы ещё не прочитали - сегодня пожалуйста посмотрите основы JavaScript и
как работать в среде WEB-разработки и отладчике. Старайтесь пользоваться
отладчиком как можно чаще, это поможет найти и исправить множество возникающих
проблем.

1. Особенности JavaScript (Обзор JS): https://learn.javascript.ru/javascript-specials
2. Консоль разработчика: https://learn.javascript.ru/devtools
    1. Отладка в браузере Chrome: https://learn.javascript.ru/debugging-chrome
    2. Обзор Chrome DevTools. Решаем основные задачи разработчика: https://htmlacademy.ru/blog/boost/tools/how-to-devtools
    3. Введение в Chrome DevTools. Панель Elements: https://htmlacademy.ru/blog/boost/tools/chrome-devtools-1
    4. Введение в Chrome DevTools. Console, Sources, Network: https://htmlacademy.ru/blog/boost/tools/chrome-devtools-2
3. JavaScript базовый синтаксис:
    1. Условное ветвление: if, '?': https://learn.javascript.ru/ifelse
    2. Циклы while и for: https://learn.javascript.ru/while-for
    3. Функции: https://learn.javascript.ru/function-basics
    4. Функции-стрелки, основы: https://learn.javascript.ru/arrow-functions-basics
4. [дополнительно] Советы по стилю кода: https://learn.javascript.ru/coding-style
5. [дополнительно] Ниндзя-код (или вредные советы): https://learn.javascript.ru/ninja-code

### Задание для самопроверки

Написать функцию `draw_flag(width, height)`, которая выводит на консоль флаг
из решеток `#` с крестом из плюсов `+`. Например:

```
>> draw_flag(9, 6)
####+####
####+####
####+####
+++++++++
####+####
####+####
```
Отправить решение сюда: https://forms.gle/uSd9nBuMAGa6ZYED7

## День Второй - работа с HTML-документом

Сегодня пора наконец-таки до конца разобраться с тем, что такое HTML-документ,
из чего он состоит и как его менять. Вспомните, что такое HTML-тег,
HTML-аттрибут, CSS-селекторы. Попробуйте искать элементы внутри HTML-документа,
менять их содержимое, аттрибуты, стили и классы.

Обратите внимание на последнюю ссылку: для написания игры на втором модуле
нужно уметь работать с координатами.

1. Браузерное окружение, спецификации: https://learn.javascript.ru/browser-environment
2. DOM-дерево: https://learn.javascript.ru/dom-nodes
3. Поиск: getElement*, querySelector*: https://learn.javascript.ru/searching-elements-dom
4. Свойства узлов: тип, тег и содержимое: https://learn.javascript.ru/basic-dom-node-properties
5. Атрибуты и свойства: https://learn.javascript.ru/dom-attributes-and-properties
6. Изменение документа: https://learn.javascript.ru/modifying-document
7. Стили и классы: https://learn.javascript.ru/styles-and-classes
8. Координаты: https://learn.javascript.ru/coordinates

### Задание для самопроверки

Дана верстка:
```html
<div>
    <h1>Hellom world!</h1>
    <ul>
        <li>A</li>
        <li>B</li>
        <li>С</li>
    </ul>
    <input type="text" name="final-text">
</div>
```
Нужно написать функцию `print_list()`, которая выведет сначала строку из
заголовка `h`, выведет содержимое списка в обратном порядке, а в конце выведет
текст введенный в input. Содержимое списка, инпута и `h1` может менятся.

Отправить решение сюда: https://forms.gle/uSd9nBuMAGa6ZYED7

## День Третий - События в браузере

Сегодня пора прочитать про основную особенность программирования в браузере,
программа в основном обрабатывает события в бразере. И тут не все так очевидно,
ознакомьтесь с такимим понятиями, как всплытие, погружение и делегирование событий.

1. Введение в браузерные события: https://learn.javascript.ru/introduction-browser-events
2. Всплытие и погружение: https://learn.javascript.ru/bubbling-and-capturing
3. Делегирование событий: https://learn.javascript.ru/event-delegation
4. Действия браузера по умолчанию: https://learn.javascript.ru/default-browser-action

### Задание для самопроверки

Дана верстка:
```html
<div><p><span>x</span><span>y</span></p></div>
```
Написать обработчик клика на `<div>`, который выведет на консоль имя тега
на который произошел клик, и если был клик на `x` должен вывестись `Mr X`,
а при клике на `y` на консоли должно быть `Ms Y`.

Отправить решение сюда: https://forms.gle/uSd9nBuMAGa6ZYED7

## День Четвертый - События Мыши и клавиатуры

Сегодня пора разобраться консретно с событиями мыши и клавиатуры. Последнее
понадобится, чтобы реализовать движение игрока по экрану.

1. Основы событий мыши: https://learn.javascript.ru/mouse-events-basics
2. Движение мыши: mouseover/out, mouseenter/leave: https://learn.javascript.ru/mousemove-mouseover-mouseout-mouseenter-mouseleave
3. Клавиатура: keydown и keyup: https://learn.javascript.ru/keyboard-events

### Задание для самопроверки

Сделать функцию-обработчик на документ, которая при нажатии на клавишу `H/h`
выводила на консоль разработчка строку: `Справка для пользователя`.

Отправить решение сюда: https://forms.gle/uSd9nBuMAGa6ZYED7

## День Пятый - Формы

Сегодня поговорим о формах, и о том как с ними работать.

1. Свойства и методы формы: https://learn.javascript.ru/form-elements
2. Фокусировка: focus/blur: https://learn.javascript.ru/focus-blur
3. События: change, input, cut, copy, paste: https://learn.javascript.ru/events-change-input
4. Отправка формы: событие и метод submit: https://learn.javascript.ru/forms-submit

### Задание для самопроверки

Дана верстка:

```html
<form name="f">
    <input type="hidden" value="secrets">
    <input name="otpravka" type="text">
</form>
```

Написать JS код, который будет вызывать авто-submit-формы, если в инпуте ввести
магическую строку `submit`.

Отправить решение сюда: https://forms.gle/uSd9nBuMAGa6ZYED7


## День Шестой - Загрузка Документа

1. Страница: DOMContentLoaded, load, beforeunload, unload: https://learn.javascript.ru/onload-ondomcontentloaded
2. Скрипты: async, defer: https://learn.javascript.ru/script-async-defer
3. Загрузка ресурсов: onload и onerror: https://learn.javascript.ru/onload-onerror

### Задание для самопроверки

Написать функцию `load_image(src)`, которая добавляет в конец `body` документа
картинку по адресу `src`. И если загрузка не удалась, выводит на консоль: `ошибка`.

Отправить решение сюда: https://forms.gle/uSd9nBuMAGa6ZYED7

## День Седьмой - Fetch И работа с сервером

1. Fetch: https://learn.javascript.ru/fetch
2. FormData: https://learn.javascript.ru/formdata
3. Fetch: ход загрузки: https://learn.javascript.ru/fetch-progress
4. Fetch: прерывание запроса: https://learn.javascript.ru/fetch-abort
5. Fetch: запросы на другие сайты: https://learn.javascript.ru/fetch-crossorigin
6. Fetch API: https://learn.javascript.ru/fetch-api
7. Объекты URL: https://learn.javascript.ru/url

Сегодня задания не будет, но если у вас есть вопросы,
можете задать их здесь: https://forms.gle/uSd9nBuMAGa6ZYED7





