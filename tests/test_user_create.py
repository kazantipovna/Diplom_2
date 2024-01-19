import allure
import pytest
import pytest_check as check

from helpers import users
from tests.data import resp_codes_msg, test_data, urls


class TestUserCreate:

    @allure.title('Успешное создание пользователя')
    @allure.description('Создаем нового пользователя и проверяем, что его данные не пустые')
    def test_create_unique_user_expected_ok(self, user):
        assert user != []

    @allure.title('Пользователь уже существует')
    @allure.description('Создаем пользователя, создаем точно такого же, и проверяем, что вернулся код ошибки')
    def test_create_existing_user_expected_error(self, user):
        resp = users.create_post_response(urls.register_url, user[0], user[1], user[2])
        assert resp_codes_msg.codes[403][0] and resp_codes_msg.codes[403][2] in resp.text
        check.equal(resp.status_code, 403)

    @allure.title('При создании не заполнено обязательное поле')
    @allure.description('Если одно из полей не заполнено, ожидаем ошибку')
    @pytest.mark.parametrize("email, password, name", test_data.register_field_missed)
    def test_create_user_empty_field(self, email, password, name):
        resp = users.create_post_response(urls.register_url, email, password, name)
        assert resp_codes_msg.codes[403][0] and resp_codes_msg.codes[403][1] in resp.text
        check.equal(resp.status_code, 403)
