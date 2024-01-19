# Diplom_2

---
#### Тесты на проверку API учебного сервиса "Stellar Burgers"

---

### Каталог tests:
* __test_get_order.py__ - тесты получение заказов конкретного пользователя:
  * **Тесты:**
    * test_get_order_without_auth - получения списка заказов без авторизации
    * test_get_order_with_auth - получения списка заказов с авторизацией
    
* __test_order_create.py__ - тесты создания заказа:
  * **Тесты:**
    * test_create_order_with_auth - создание бургера авторизованным пользователем
    * test_create_burger - создание заказа с количеством ингредиентов 0, 1, 10
    * test_create_order_incorrect_hash - создание заказа с неверными хешами
    
* __test_user_change.py__ - тесты логина курьера:
  * **Тесты:**
    * test_change_data_without_auth_expected_error - редактирование пользователя без авторизации
    * test_change_data_with_auth_expected_ok - редактирование пользователя с авторизацией

* __test_user_create.py__ - тесты цветов при заказе:
  * **Тесты:**
    * test_create_unique_user_expected_ok - успешное создание пользователя
    * test_create_existing_user_expected_error - пользователь уже существует
    * test_create_user_empty_field - при создании не заполнено обязательное поле

* __test_user_login.py__ - тест списка заказов курьера:
  * **Тесты:**
    * test_login_user_expected_or - тест успешного логина
    * test_login_incorrect_user_expected_error - тест неуспешного логина

* __conftest.py__ - фикстуры


  #### Каталог tests/data:
  * __resp_codes_msg.py__ - сообщения кодов для сверки результатов
  * __test_data.py__ - прочие вспомогательные тестовые данные
  * __urls.py__ - ссылки-ручки

### Каталог helpers:
* __orders.py__ - вспомогательные методы для тестов по бургеру 
* __users.py__ - вспомогательные методы для тестов по пользователю
