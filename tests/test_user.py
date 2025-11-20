import pytest

from api.pet_api import PetApi
from api.user_api import UserApi

class TestStore:

    @pytest.fixture
    def api(self):
        return UserApi()

    def test_create_user(self, api):
        new_user = {
            "id": 1,
            "username": "testuser",
            "firstName": "Test",
            "lastName": "User",
            "email": "test@email.com",
            "password": "password123",
            "phone": "123456789",
            "userStatus": 1
        }
        response = api.create_user(new_user)
        assert response.status_code == 200

    def test_login_user(self, api):
        new_user = {
            "id": 0,
            "username": "string",
            "firstName": "string",
            "password": "string"
        }
        response = api.create_user(new_user)
        assert response.status_code == 200

        response = api.login_user(username="string", password="string")
        assert response.status_code == 200


    def test_logout_user(self, api):

        response = api.logout_user()
        assert response.status_code == 200

    def test_update_user(self, api):
        new_user = {
            "username": "old_username",
            "firstName": "Old Name",
            "email": "old@email.com"
        }
        create_response = api.create_user(new_user)
        assert create_response.status_code == 200

        updated_user = {
            "username": "new_username",
            "firstName": "New Name",
            "email": "new@email.com"
        }
        update_response = api.update_user("old_username", updated_user)
        assert update_response.status_code == 200


    def test_delete_user(self, api):
        new_user = {
            "username": "testuser"
        }
        create_response = api.create_user(new_user)
        assert create_response.status_code == 200

        delete_response = api.delete_user("user_to_delete")
        assert delete_response.status_code in [200, 404]


    def test_create_users_with_array(self, api):
        users_array = [
            {
                "username": "minimal1",
                "firstName": "Minimal",
                "lastName": "One"
            },
            {
                "username": "minimal2",
                "firstName": "Minimal",
                "lastName": "Two"
            }
        ]
        response = api.create_users_with_array(users_array)
        assert response.status_code == 200