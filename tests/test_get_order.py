import allure
import pytest_check as check

from helpers import users
from tests.data import resp_codes_msg, urls


class TestGetOrder:

    @allure.title('Тест получения списка заказов без авторизации')
    @allure.description('Получение заказов неавторизованного пользователя, проверяем, что вернулся код ошибки')
    def test_get_order_without_auth(self, user):
        resp = users.create_get_response(urls.orders_url, None, user[0], user[1], user[2])
        assert resp_codes_msg.codes[401][0] and resp_codes_msg.codes[401][2] in resp.text
        check.equal(resp.status_code, 401)

    @allure.title('Тест получения списка заказов с авторизацией')
    @allure.description('Получение заказов авторизованного пользователя')
    def test_get_order_with_auth(self, user):
        resp = users.create_get_response(urls.orders_url, user[3], user[0], user[1], user[2])
        assert resp_codes_msg.codes[200][0] in resp.text
        check.equal(resp.status_code, 200)
