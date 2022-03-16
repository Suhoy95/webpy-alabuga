${"#"} Модуль 1: Разработка на стороне сервера

${"##"} Содержание

Данный тестовый проект состоит из следующих файлов:

1. `task_1.md` – Задание
2. Верстка:
    1. `index.html` - Главная страница
    2. `login.html` - Авторизация
    3. `registration.html` - Регистрация
    4. `new.html` - Создание Бага
    5. `bug.html` - Обсуждение Бага

${"##"} Введение

1. Ваша задача разработать небольшой сервис для Bug-трекинга.
2. Вам предоставляются заранее сверстанные макеты всех страниц сервиса.
3. Вам необходимо реализовать следующий функционал:
    1. Регистрация, авторизация и выход пользователей
    2. Разграничение пользователей по ролям (гость, пользователь и администратор)
    3. Создание Bug-ветки обсуждения
    4. Создание комментариев в Bug-ветках
    5. Возможность изменения статуса Bug-ветки (для администратора)

${"##"} Описание проекта и задач

${"###"} Регистрация

4. Гости должны иметь возможность зарегистрироваться в сервисе.
5. Для этого им требуется ввести следующие данные на странице регистрации:
    1. Никнейм – обязательное поле, уникальное
    2. Email – обязательное поле, уникальное, email
    3. Пароль – обязательное поле
    4. Повтор пароля – обязательное поле, должно совпадать с паролем
6. Данные с формы должны валидироваться на стороне сервера
7. и в случае ошибки валидации необходимо отобразить соответствующие ошибки на форме.
8. Все зарегистрировавшиеся пользователи должны автоматически получать роль пользователя.
9. В случае успешной регистрации, пользователь должен быть перенаправлен на страницу Авторизации.
10. Страница регистрации должна находиться по адресу `${domain}${m1_register_path}`.
11. Ссылка на страницу пользователя должна быть на всех страницах сайта, пока пользователь **не авторизован**.

${"###"} Авторизация и Выход

11. Пользователи должны иметь возможность авторизоваться в сервисе используя Никнейм и пароль.
12. Все ошибки валидации должны отображаться.
13. Страница Авторизации должна находится по адресу `${domain}${m1_auth_path}`.
14. Ссылка на Авторизацию должна быть на всех страницах сайта, пока пользователь **не авторизован**.
15. В случае успешной авторизации Пользователь должен быть перенаправлен на Главную страницу.
16. Авторизовавшиеся пользователи должны иметь возможность выйти из сервиса перейдя по адресу `${domain}/logout/`.
17. Ссылка на Выход из системы должна быть на всех страницах, пока пользователь Авторизован.
18. В случае успешного выхода из системы, пользователь должен быть перенаправлен на страницу Авторизации.

${"###"} Создание Bug-ветки обсуждения

19. Пользователь должен иметь возможность создать новую Bug-Ветку обсуждения.
20. Страница Создания Bug-ветки должна находиться по адресу: `${domain}${m1_create_path}`
21. Ссылка на Создание Bug-ветки должна быть на всех страницах, пока пользователь Авторизован.
22. На странице Создания Bug-ветки обсуждения Пользователю необходимо заполнить следующую форму:
    1. Название Bug-ветки – обязательное поле, не более 50 символов
    2. Описание Bug-Ветки – обязательное поле, не более ${m1_charnum} символов
    3. Категория Bug-Ветки - обязательное поле, выбор из вариантов: `Улучшение`, `Ошибка`, `Критическая Ошибка`
23. В случае ошибок валидации необходимо отобразить сообщения об ошибках.
24. Созданная Bug-Ветка должна иметь дату и время создания.
25. У Bug-Ветки должен быть один из следующих статусов: `Открыт`, `В работе`, `Закрыт`.
26. По умолчанию у Bug-Ветки должен быть статус `Открыт`.
27. После успешного создания Bug-ветки пользователь должен перенаправляться на её страницу по адресу: `${domain}${m1_show_path}`

${"###"} Главная страница

28. На главной странице должно выводиться:
    1. Количество Bug-веток со статусом `Открыто`
    2. Количество Bug-веток со статусом `В работе`
    3. Количество Bug-веток со статусом `Закрыто`
29. На главной странице должны выводиться все задачи сос статусами `Открыто` и `В работе`.
30. Задачи с категорией `Критическая Ошибка` должны выводиться первыми
31. Задачи должны быть отсортированы по времени с учетом пункта 31. В начале идут новые Bug-ветки
32. Каждая Bug-ветка на главной странице должна иметь:
    1. Название
    2. Дату Создания в формате  дд.мм.гггг чч:мм
    3. Никнейм пользователя, создавшего Bug-ветку
    4. Статус Bug-ветки
    5. Категорию Bug-ветки
33. На главной странице, Пользователи и гости должны иметь возможность перейти
на страницу с Bug-ветки по адресу: `${domain}${m1_show_path}`.

${"###"} Обсуждение Bug-ветки

33. Все Созданные Bug-ветки должны быть доступны по адресу `${domain}${m1_show_path}`,
где `id` - уникальный номер Bug-ветке, задаваемый при создании
34. На данной странице должна отображаться следующая информация:
    1. Название Bug-ветки
    2. Описание Bug-ветки
    3. Статус Bug-Ветки
    4. Категория Bug-Ветки
    5. Дата и время создания Bug-Ветки в формате дд.мм.гггг чч:мм
    6. Комментарии, где каждый комментарий имеет:
        1. Текст комментария
        2. Имя автора
        3. Дату и время в формате дд.мм.гггг чч:мм
35. Авторизованный пользователь должен иметь возможность оставлять комментарии под видеороликом,
если её статус не `Закрыто`
36. Комментарии должны быть отсортированы по новизне (сначала новые).
37. Администратор и Автор Bug-ветки должны иметь возможность менять Статус Bug-Ветки.

${"##"} Инструкции для участника

38. Ваша работа должна быть доступна по адресу: `http://${domain}`,
39. Создайте учетную запись администратора со следующими учетными данными:
    1. Логин: admin
    2. Пароль: qweASD123
40. Вам предоставляются следующие Фреймворки: Django
41. Для публикации работы, файлы игры нужно разместить в директории `/home/std${std_num}/mar/module1/`.
42. Данные для подключения и настройки сервера должны быть проверены и предоставлены заранее