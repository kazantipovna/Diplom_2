import allure
import requests

from data import urls


@allure.step('Получаем хеш ингредиента из общего списка:')
def get_ingredients_hash(ingr_num):
    response = requests.get(urls.ingr_url)
    ingredient_hash = response.json()['data'][ingr_num]['_id']
    return ingredient_hash


@allure.step('Составляем payload из переданного количества ингредиентов:')
def create_burger_payload(ingr_count):
    for ingr_count in range(ingr_count):
        payload = {"ingredients": [get_ingredients_hash(ingr_count)]}
        return payload


@allure.step('Создаем пост запрос для создания бургера:')
def create_post_burger_response(ingr_count):
    payload = create_burger_payload(ingr_count)
    response = requests.post(urls.orders_url, data=payload)
    return response
