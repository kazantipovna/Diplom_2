import allure
import pytest
import pytest_check as check
import requests

from helpers import orders, users
from tests.data import resp_codes_msg, test_data, urls


class TestOrderCreate:

    @allure.title('Тест создания бургера авторизованным пользователем')
    @allure.description('Создаем бургер авторизованным пользователем')
    def test_create_order_with_auth(self, user):
        resp = requests.post(urls.orders_url, headers=users.create_headers(user[3]),
                             data=orders.create_burger_payload(1))
        assert resp_codes_msg.codes[200][0] in resp.text
        check.equal(resp.status_code, 200)

    @allure.title('Тест создания заказа с количеством ингредиентов')
    @allure.description('Если ингредиентов 0, ожидаем ошибку 400, в остальных случаях бургер создается, ожидаем 200')
    @pytest.mark.parametrize("ingr_count", [0, 1, 10])
    def test_create_burger(self, ingr_count):
        resp = orders.create_post_burger_response(ingr_count)
        if ingr_count == 0:
            assert resp_codes_msg.codes[400][0] and resp_codes_msg.codes[400][1] in resp.text
            check.equal(resp.status_code, 400)
        else:
            assert resp_codes_msg.codes[200][0] in resp.text
            check.equal(resp.status_code, 200)

    @allure.title('Тест создания заказа с неверными хешами')
    @allure.description('Создаем бургер с неверным хешем ингредиентов, проверяем, что вернется ошибка 500')
    def test_create_order_incorrect_hash(self):
        resp = requests.post(urls.orders_url, data={"ingredients": test_data.incorrect_hash})
        print(resp.text)
        assert resp_codes_msg.codes[500][0] in resp.text
        check.equal(resp.status_code, 500)
