import mimetypes
import os

import requests


class UserApi:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def create_user(self, user_data):
        #Создание пользователя
        response = requests.post(f"{self.base_url}/user", json=user_data)
        return response

    def login_user(self, username, password):
        #Вход по логину и паролю
        user_creds={'username':username, 'password':password}
        response = requests.get(f"{self.base_url}/user/login", params=user_creds)
        return response

    def logout_user(self):
        #Вход по логину и паролю
        response = requests.get(f"{self.base_url}/user/logout")
        return response

    def update_user(self, username, user_data):
        #Обновление данных пользователя
        response = requests.put(f"{self.base_url}/user/{username}", json=user_data)
        return response

    def get_user_by_name(self, username):
        response = requests.get(f"{self.base_url}/user/{username}")
        return response

    def delete_user(self, username):
        response = requests.delete(f"{self.base_url}/user/{username}")
        return response

    def create_users_with_array(self, users_array):
        response = requests.post(f"{self.base_url}/user/createWithArray", json=users_array)
        return response

