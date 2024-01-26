import allure
import requests
from faker import Faker

from tests.data import urls


def create_test_user():
    """Создает словарь с данными тестового пользователя"""
    fake_data = Faker()
    test_user = {'email': fake_data.email(),
                 'password': fake_data.password(),
                 'name': fake_data.user_name()}
    return test_user


@allure.step('Создаем пользователя:')
def register_new_user():
    """Создаем пользователя, записываем его данные в список и возвращаем этот список"""
    user_data = []
    user = create_test_user()

    payload = {
        "email": user['email'],
        "password": user['password'],
        "name": user['name']
    }

    response = requests.post(urls.register_url, data=payload)

    if response.status_code == 200:
        user_data.append(user['email'])
        user_data.append(user['password'])
        user_data.append(user['name'])
        user_data.append(response.json()['accessToken'])

    with allure.step(f'Создан пользователь email = {user_data[0]}, password = {user_data[1]}, '
                     f'name = {user_data[2]}, accessToken = {user_data[3]}'):
        return user_data


@allure.step('Удаляем пользователя:')
def delete_user(access_token):
    header = create_headers(access_token)
    response = requests.delete(urls.user_url, headers=header)
    return response


@allure.step('Выполняем POST запрос:')
def create_post_response(url, email, password, name=None):
    """Выполняет post запрос для логина или создания пользователя"""
    payload = create_payload(email, password, name)
    response = requests.post(url, data=payload)
    return response


@allure.step('Выполняем PATCH запрос:')
def create_patch_response(url, access_token=None, email=None, password=None, name=None):
    """Выполняет patch запрос для изменения данных пользователя"""
    header = create_headers(access_token)
    payload = create_payload(email, password, name)
    response = requests.patch(url, headers=header, data=payload)
    return response


@allure.step('Выполняем GET запрос:')
def create_get_response(url, access_token=None, email=None, password=None, name=None):
    """Выполняет get запрос для логина или создания пользователя"""
    header = create_headers(access_token)
    payload = create_payload(email, password, name)
    response = requests.get(url, headers=header, data=payload)
    return response


def create_payload(email, password, name):
    """Заполняет payload из данных пользователя"""
    payload = {"email": email, "password": password, "name": name}
    return payload


def create_headers(access_token):
    """Заполняет хедер авторизации токеном"""
    headers = {"authorization": access_token}
    return headers
