import allure
import data
import helpers
from methods.user_methods import UserMethods

@allure.feature("Изменение данных пользователя")
class TestUserUpdate:

    @allure.title("Изменение имени с авторизацией")
    def test_update_user_name_with_auth(self, api_client, created_user):
        access_token = created_user["access_token"]
        new_name = helpers.generate_unique_name()
        update_data = {"name": new_name}

        response = UserMethods.update_user(api_client, access_token, update_data)

        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_name

    @allure.title("Изменение email с авторизацией")
    def test_update_user_email_with_auth(self, api_client, created_user):
        access_token = created_user["access_token"]
        new_email = helpers.generate_unique_email()
        update_data = {"email": new_email}

        response = UserMethods.update_user(api_client, access_token, update_data)

        assert response.status_code == 200
        assert response.json()["user"]["email"] == new_email

    @allure.title("Изменение данных без авторизации")
    def test_update_user_without_auth(self, api_client):
        update_data = {"name": helpers.generate_unique_name()}
        url = data.BASE_URL + data.USER_ENDPOINT

        response = api_client.patch(url, json=update_data)

        assert response.status_code == 401
        assert response.json()["success"] is False