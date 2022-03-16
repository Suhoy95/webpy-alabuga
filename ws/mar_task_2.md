# Модуль 2: Разработка на стороне клиента

${"##"} Содержание

Данный тестовый проект состоит из следующих файлов:

1. `task.md` – Задание
2. `maps.json` – JSON-массив с картами
3. `index.html` - Верстка Экрана Входа
4. `game.html` - Верстка Экрана Игры
5. `results.html` - Верстка Экрана Результатов

${"##"} Введение

К вам обратилась компания по разработке игр для веб-сайтов.
Компания просит помочь в разработке веб-игры.
Вам предоставляется вся необходимая верстка.

> Ваша задача – только клиентское программирование.

Время на выполнение: 1,5ч.

${"##"} Описание проекта и задач - Bug-Catcher

${"###"} Экран входа

1. При переходе на сайт с игрой должен быть отображен экран входа.
2. На экране входа располагается поле, где пользователь может ввести свое имя и
выбрать одну из предложенных карт.
3. Карты выводятся из `json`-файла `maps.json` с помощью запроса.
4. После карты и ввода имени, пользователь может нажать на кнопку `"Начать игру"`.
5. Имя пользователя может состоять только из латинских букв верхнего и нижнего регистра,
знака дефиса, подчеркивания и цифр.
6. Пока не выбрана карта и/или не введено имя пользователя,
а также если имя пользователя не введено корректно, кнопка `"Начать игру"`
должна находится в отключенном состоянии.
7. После выполнения пункта 4, пользователь должен перейти на `Игровой экран`.

${"###"} Игровой экран

8. На игровом экране должна отображаться следующая информация:
    1. Имя, введенное пользователем
    2. Текущее время в системе в формате `чч:мм:сс`
    3. Время прошедшее с начала игры в формате `мм:сс`, в начале равно `00:00`
    4. Количество Багов (баллов), пойманных игроком в игре, в начале равно нулю.
    5. Пользователь, располагающийся с левого края.
9. Пользователь должен иметь возможность перемещать игрока с помощью нажатия на
стрелки.
10. Игрок не должен выходить за верхний, левый и нижний край карты.
11. При выходе за правый край карты игры заканчивается.
12. Каждые 3 секунды на поле появляется Один Красный Bug, и один Зеленый.
13. Вновь появившиеся Bug-и не должны пересекаться с Игроком.
14. При столкновении с Зеленым Bug-ом Игрок получает 1 балл.
15. При столкновении с Красным Bug-ом Игрок проигрывает и игры заканчивается.
16. Должна быть возможность поставить игру на паузу нажав кнопку `ESC`.
17. Повторное нажатие должно продолжить игру.
18. После завершения Игры, Пользователь должен увидеть экран с результатами

${"###"} Экран с результатами

19. На экране с результатами необходимо отобразить статистику игры:
    1. Время, которое игрок продержался в игре
    2. Количество набранных баллов
    3. Проиграл или выиграл Игрок, в зависимости от того как игра Завершилась
        - Выход через правый край - Пользователь Выиграл
        - Столкновение с Красным Bug-ом - Пользователь Проиграл
20. На экране с результатами есть кнопка «Играть сначала» при клике, на которую игра должна перейти на "Экран входа".
21. При переходе на экран входа, имя предыдущего игрока должно сохранятся.

${"##"} Инструкции для участника

22. Ваша работа должна быть доступна по адресу: `http://${domain}/module2/`,
23. Для публикации работы, файлы игры нужно разместить в
директории `/home/std${std_num}/mar/module2/`.
24. Логины и пароли должны быть предоставлены заранее.