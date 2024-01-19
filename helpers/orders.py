import requests

from tests.data import urls


def get_ingredients_hash(ingr_num):
    """Получает хеш ингредиента из общего списка"""
    response = requests.get(urls.ingr_url)
    ingredient_hash = response.json()['data'][ingr_num]['_id']
    return ingredient_hash


def create_burger_payload(ingr_count):
    """Составляет payload из переданного количества ингредиентов"""
    for ingr_count in range(ingr_count):
        payload = {"ingredients": [get_ingredients_hash(ingr_count)]}
        return payload


def create_post_burger_response(i):
    """Создает пост запрос для создания бургера"""
    payload = create_burger_payload(i)
    response = requests.post(urls.orders_url, data=payload)
    return response
