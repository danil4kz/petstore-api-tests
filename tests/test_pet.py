import pytest
from api.pet_api import PetApi

class TestPet:

    @pytest.fixture
    def api(self):
        return PetApi()

    def test_create_pet(self, api):
        #Тест на создание питомца
        new_pet = {
            "name": "Мурзик",
            "photoUrls": ["url1", "url2"]
        }
        response = api.create_pet(new_pet)
        assert response.status_code == 200
        pet_data = response.json()
        assert pet_data['name'] == new_pet['name']
        assert pet_data['photoUrls'] == new_pet['photoUrls']

        new_pet = {
            "name": "Мурзик",
            "photoUrls": ["url1", "url2"],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
        }
        response = api.create_pet(new_pet)
        assert response.status_code == 200
        pet_data = response.json()
        assert pet_data['name'] == new_pet['name']
        assert pet_data['photoUrls'] == new_pet['photoUrls']

        new_pet = {
            "name": "Bob",
            "photoUrls": ["url3", "url4"],
            "tags": [
                {
                    "id": 122,
                    "name": "string"
                }
            ],
        }
        response = api.create_pet(new_pet)
        assert response.status_code == 200
        pet_data = response.json()
        assert pet_data['name'] == new_pet['name']
        assert pet_data['photoUrls'] == new_pet['photoUrls']


    def test_get_pet_by_id(self, api):
        #Тест на получение питомца по ID
        new_pet = {
            "name": "Мурка",
            "photoUrls": ["photo_url"]
        }
        create_response = api.create_pet(new_pet)
        pet_id = create_response.json()['id']

        response = api.get_pet_by_id(pet_id)
        assert response.status_code in [200, 404]

        if response.status_code == 200:
            pet_data = response.json()
            assert pet_data['name'] == "Мурка"

            new_pet = {
                "name": "Сергоня",
                "photoUrls": ["photo_url"]
            }
            create_response = api.create_pet(new_pet)
            pet_id = create_response.json()['id']

            response = api.get_pet_by_id(pet_id)
            assert response.status_code in [200, 404]

            if response.status_code == 200:
                pet_data = response.json()
                assert pet_data['name'] == "Сергоня"


    def test_update_pet(self, api):
        #Тест на обновление питомца (PUT)
        new_pet = {
            "id": 12345,
            "name": "СтароеИмя",
            "photoUrls": ["old_url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200

        updated_pet = {
            "id": 12345,
            "name": "НовоеИмя",
            "photoUrls": ["new_url"]
        }
        update_response = api.update_pet(updated_pet)
        assert update_response.status_code == 200

        updated_data = update_response.json()
        assert updated_data['name'] == "НовоеИмя"

        updated_pet = {
            "id": 12345,
            "name": "НовоеИмя питомца с категорией",
            "photoUrls": ["new_url1"],
            "category": {
                "id": 1,
                "name": "dogs"
            }
        }
        update_response = api.update_pet(updated_pet)
        assert update_response.status_code == 200

        updated_data = update_response.json()
        assert updated_data["category"] == {
            "id": 1,
            "name": "dogs"
        }

        updated_pet = {
            "id": 12345,
            "name": 555,
            "photoUrls": ["new_url"]
        }
        update_response = api.update_pet(updated_pet)
        assert update_response.status_code == 200

        updated_data = update_response.json()
        assert updated_data['name'] == '555'


    def test_delete_pet(self, api):
        #Тест на удаление питомца

        new_pet = {
            "id": 12345,
            "name": "Старик",
            "photoUrls": ["url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200
        response = api.delete_pet_by_id(12345)
        assert response.status_code in [200, 404]


    def test_find_pets_by_status(self, api):
        #Тест поиска питомцев по статусу
        response = api.find_pets_by_status("available")
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)

        response = api.find_pets_by_status("123")
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list)


    def test_upload_image(self, api):
        #Тест на загрузку изображения питомца
        new_pet = {
            "id": 12345,
            "name": "Старик",
            "photoUrls": ["url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200
        response = api.upload_image(pet_id=12345, image_path="images.jpeg",additional_metadata="abc")
        assert response.status_code == 200

        new_pet = {
            "id": 12345,
            "name": "Старик",
            "photoUrls": ["url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200
        response = api.upload_image(pet_id=12345)
        assert response.status_code == 415


    def test_update_pet_form(selfself, api):
        #Тест на обновления питомца по форме
        new_pet = {
            "id": 12345,
            "name": "Старикашка",
            "photoUrls": ["url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200
        response = api.update_pet_form(pet_id=12345)
        assert response.status_code == 200

        new_pet = {
            "id": 12345,
            "name": "Старикашка",
            "photoUrls": ["url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200
        response = api.update_pet_form(pet_id=12345, name="Маша")
        assert response.status_code == 200

        new_pet = {
            "id": 12345,
            "name": "Старикашка",
            "photoUrls": ["url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200
        response = api.update_pet_form(pet_id=12345, status="sold")
        assert response.status_code == 200

        new_pet = {
            "id": 12345,
            "name": "Старикашка",
            "photoUrls": ["url"]
        }
        create_response = api.create_pet(new_pet)
        assert create_response.status_code == 200
        response = api.update_pet_form(pet_id=12345, name="Маша", status="sold")
        assert response.status_code == 200
