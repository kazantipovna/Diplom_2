import allure
import requests
import random
import string

from tests.data import urls


@allure.step('Создаем пользователя:')
def register_new_user():
    """Создаем пользователя, записываем его данные в список и возвращаем этот список"""
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    user_data = []

    email = generate_random_string(10) + '@yq.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(urls.register_url, data=payload)

    if response.status_code == 200:
        user_data.append(email)
        user_data.append(password)
        user_data.append(name)
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
