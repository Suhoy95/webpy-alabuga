# 202202190137 Валидация формы ввода Имени пользователя

Третий этап реализации [формы входа](202202181645-login-form-m2-ws.md),
[второго модуля по WorldSkills КОД 1.3](202202150946-WS-module-2.md).

1. В последних версиях HTML5 у input-ов появилось много полезных атрибутов для
валидирования формы на стороне клиента:
    - Чтобы пользователь не указал пустое имя, нам поможет атрибут
    `required` - говорящий браузеру, что данное поле обязательно для заполнения
    - Чтобы пользователь вводил только буквы/цифры и не более 20-ти,
    мы можем воспользоваться атрибутом `pattern`, указывающим регулярное выражение,
    которому должно соответствовать введенное значение
    - Чтобы при валидации возникала понятное пользователю описание, что нужно ввести в это поле
    нам поможет атрибут title.

![](2022-02-19-02-12-56.png)

2. Проверяем:

![](2022-02-19-02-13-39.png)

## Следующий шаг

Переходим к [обработке отправки формы](202202190215-submit-login-form-m2-ws.md)