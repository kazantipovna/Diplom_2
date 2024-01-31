import allure
import pytest

from helpers import users
from data import test_data
from data import resp_codes_msg, urls


@allure.feature('Изменение данных пользователя')
class TestUserChange:

    @allure.title('Изменение пользователя без авторизации')
    @allure.description('Изменение данных пользователя без авторизации, проверяем, что вернулся код ошибки')
    @pytest.mark.parametrize("email, password, name", test_data.check_changes)
    def test_change_data_without_auth_expected_error(self, user, email, password, name):
        resp = users.create_patch_response(urls.user_url, None, email, password, name)
        assert resp_codes_msg.codes[401][0] and resp_codes_msg.codes[401][2] in resp.text and resp.status_code == 401

    @allure.title('Изменение пользователя с авторизацией')
    @allure.description('Изменение данных пользователя с авторизацией, изменения успешны')
    @pytest.mark.parametrize("email, password, name", test_data.check_changes)
    def test_change_data_with_auth_expected_ok(self, user, email, password, name):
        resp = users.create_patch_response(urls.user_url, user[3], email, password, name)
        assert resp_codes_msg.codes[200][0] in resp.text and resp.status_code == 200
