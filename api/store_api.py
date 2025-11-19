import mimetypes
import os

import requests


class StoreApi:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def get_inventory(self):
        #Поиск  инвентаря по статусу
        response = requests.get(f"{self.base_url}/store/inventory")
        return response

    def create_order(self, order_data):
        #Создание заказа
        response = requests.post(f"{self.base_url}/store/order", json=order_data)
        return response

    def get_order_by_id(self, order_id):
        #Получение заказа по ID
        response = requests.get(f"{self.base_url}/store/order/{order_id}")
        return response

    def delete_order_by_id(self, order_id):
        #Удаление заказа
        response = requests.delete(f"{self.base_url}/store/order/{order_id}")
        return response
