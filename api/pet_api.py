import mimetypes
import os

import requests


class PetApi:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def create_pet(self, pet_data):
        #Создание питомца
        response = requests.post(f"{self.base_url}/pet", json=pet_data)
        return response

    def get_pet_by_id(self, pet_id):
        #Получение питомца по ID
        response = requests.get(f"{self.base_url}/pet/{pet_id}")
        return response

    def update_pet(self, pet_data):
        #Обновление данных питомца
        response = requests.put(f"{self.base_url}/pet", json=pet_data)
        return response

    def delete_pet_by_id(self, pet_id):
        #Удаление питомца
        response = requests.delete(f"{self.base_url}/pet/{pet_id}")
        return response

    def find_pets_by_status(self, status):
        #Поиск  питомцев по статусу
        params = {"status": status}
        response = requests.get(f"{self.base_url}/pet/findByStatus", params=params)
        return response

    def upload_image(self, pet_id, image_path: str = None, additional_metadata: str | None = None):
        #Загрузка изображения питомца
        data = {}
        if additional_metadata is not None:
            data["additionalMetadata"] = additional_metadata
        if image_path is None:
            response = requests.post(f"{self.base_url}/pet/{pet_id}/uploadImage", data=data)
            return response

        mime_type, _ = mimetypes.guess_type(image_path)
        if mime_type is None:
            mime_type = "application/octet-stream"

        with open(image_path, "rb") as f:
            files = {
                "file": (os.path.basename(image_path), f, mime_type)
            }

            response = requests.post(f"{self.base_url}/pet/{pet_id}/uploadImage", data=data, files=files)
            return response

    def update_pet_form(self, pet_id: int, name: str | None = None, status: str | None = None):
        #Обновление данных питомца по форме
        data: dict[str, str] = {}
        if name is not None:
            data["name"] = name
        if status is not None:
            data["status"] = status

        response = requests.post(f"{self.base_url}/pet/{pet_id}", data=data)
        return response
