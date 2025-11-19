import pytest

from api.pet_api import PetApi
from api.store_api import StoreApi

class TestStore:

    @pytest.fixture
    def api(self):
        return StoreApi()

    def test_get_inventory(self, api):
        #Тест поиска заказа по статусу
        new_pet = {
            "name": "Мурзик",
            "photoUrls": ["url1", "url2"],
            "status": '777'
        }
        response = PetApi().create_pet(new_pet)

        response = api.get_inventory()
        assert response.status_code == 200
        order = response.json()
        assert isinstance(order, dict)
        assert '777' in order.keys()
        assert order['777'] == 1


    def test_create_order(self, api):
        #Тест на создание заказа
        new_order = {
            "id": 1,
            "petId": 2,
            "quantity": 3,
            "complete": True
        }
        response = api.create_order(new_order)
        assert response.status_code == 200
        order_data = response.json()
        assert order_data['id'] == new_order['id']
        assert order_data['petId'] == new_order['petId']
        assert order_data['quantity'] == new_order['quantity']

        new_order = {
            "id": 32,
            "petId": 23,
            "quantity": 1,
            "status": "placed"
        }
        response = api.create_order(new_order)
        assert response.status_code == 200
        order_data = response.json()
        assert order_data['id'] == new_order['id']
        assert order_data['petId'] == new_order['petId']
        assert order_data['quantity'] == new_order['quantity']
        assert order_data['status'] == new_order['status']


    def test_get_order_by_id(self, api):
        #Тест на получение заказа по ID
        new_order = {
            "id": 1,
            "petId": 2,
            "quantity": 3
        }
        create_response = api.create_order(new_order)
        order_id = create_response.json()['id']

        response = api.get_order_by_id(order_id)
        assert response.status_code in [200, 404]

        if response.status_code == 200:
            order_data = response.json()
            assert order_data['id'] == 1


    def test_delete_order(self, api):
        #Тест на удаление заказа

        new_order = {
            "id": 1,
            "petId": 2,
            "quantity": 3
        }
        create_response = api.create_order(new_order)
        assert create_response.status_code == 200
        response = api.delete_order_by_id(1)
        assert response.status_code in [200, 404]