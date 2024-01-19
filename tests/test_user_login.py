import allure
import pytest_check as check

from helpers import users
from tests.data import resp_codes_msg, urls


class TestUserLogin:

    @allure.title('Тест успешного логина')
    @allure.description('Тест успешного логина пользователя')
    def test_login_user_expected_or(self, user):
        resp = users.create_post_response(urls.login_url, user[0], user[1])
        assert resp_codes_msg.codes[200][0] in resp.text
        check.equal(resp.status_code, 200)

    @allure.title('Тест неуспешного логина')
    @allure.description('Тест неуспешного логина пользователя - с неверным логином и паролем')
    def test_login_incorrect_user_expected_error(self):
        resp = users.create_post_response(urls.login_url, "Unregister_user_login", "Unregister_user_pass")
        assert resp_codes_msg.codes[401][0] and resp_codes_msg.codes[401][1] in resp.text
        check.equal(resp.status_code, 401)
