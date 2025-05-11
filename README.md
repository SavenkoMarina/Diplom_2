# Diplom_2

Чтобы запустить все тесты нужно выполнить команду:
```bash
PYTHONPATH=. pytest tests/*
```

Создание пользователя 
1. test_create_duplicate_user - Создание пользователя который уже зарегистрирован
2. test_create_skip_required_field - Создание пользователя с пропущенными обязательными полями

Логин пользователя
1. test_login_success - Логин под существующим пользователем
2. test_login_failed - Логин с неверным логином или паролем

Изменение данных пользователя
1. test_update_user_success - Изменение пользователя с авторизаций
2. test_update_user_failed - Изменение пользователя без авторизаций

Создание заказа
1. test_create_order_success - Создание заказа
2. test_create_order_unauthorized - Создание заказа неавторизованным пользователем
3. test_create_order_without_ingredients - Создание заказа без ингридиентов
4. test_create_order_with_invalid_ingredients - Создание заказа с неверным хэшем ингридиентов

Получение заказов конкретного пользователя
1. test_get_order_authorized - Получение заказа авторизованного пользователя
2. test_get_order_unauthorized - Получение заказа не авторизованного пользователя

