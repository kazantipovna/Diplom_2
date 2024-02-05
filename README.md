## Дипломный проект. Задание 2: API-тесты

---
#### Тесты на проверку API учебного сервиса "Stellar Burgers"

---

### Каталог tests:
* `test_get_order.py` - тесты получение заказов конкретного пользователя:
  * **Тесты:**
    * test_get_order_without_auth - получения списка заказов без авторизации
    * test_get_order_with_auth - получения списка заказов с авторизацией
    
* `test_order_create.py` - тесты создания заказа:
  * **Тесты:**
    * test_create_order_with_auth - создание бургера авторизованным пользователем
    * test_create_burger - создание заказа с количеством ингредиентов 0, 1, 10
    * test_create_order_incorrect_hash - создание заказа с неверными хешами
    
* `test_user_change.py` - тесты логина курьера:
  * **Тесты:**
    * test_change_data_without_auth_expected_error - редактирование пользователя без авторизации
    * test_change_data_with_auth_expected_ok - редактирование пользователя с авторизацией

* `test_user_create.py` - тесты цветов при заказе:
  * **Тесты:**
    * test_create_unique_user_expected_ok - успешное создание пользователя
    * test_create_existing_user_expected_error - пользователь уже существует
    * test_create_user_empty_field - при создании не заполнено обязательное поле

* `test_user_login.py` - тест списка заказов курьера:
  * **Тесты:**
    * test_login_user_expected_or - тест успешного логина
    * test_login_incorrect_user_expected_error - тест неуспешного логина


* `conftest.py` - фикстуры


  #### Каталог tests/data:
  * `resp_codes_msg.py` - сообщения кодов для сверки результатов
  * `test_data.py` - прочие вспомогательные тестовые данные
  * `urls.py` - ссылки-ручки

### Каталог helpers:
* `orders.py` - вспомогательные методы для тестов по бургеру 
* `users.py` - вспомогательные методы для тестов по пользователю
