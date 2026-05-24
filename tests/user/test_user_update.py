import allure
import helpers
from methods import user_methods

@allure.feature("Изменение данных пользователя")
class TestUserUpdate:

    @allure.title("Изменение данных с авторизацией - возвращает 200")
    def test_update_user_with_auth_returns_200(self, api_client, created_user):
        access_token = created_user["access_token"]
        update_data = {"name": helpers.generate_unique_name()}
        
        response = user_methods.update_user(api_client, access_token, update_data)
        
        assert response.status_code == 200

    @allure.title("Изменение данных с авторизацией - обновляется имя")
    def test_update_user_name_with_auth_success(self, api_client, created_user):
        access_token = created_user["access_token"]
        new_name = helpers.generate_unique_name()
        update_data = {"name": new_name}
        
        response = user_methods.update_user(api_client, access_token, update_data)
        
        assert response.json()["user"]["name"] == new_name

    @allure.title("Изменение данных с авторизацией - обновляется email")
    def test_update_user_email_with_auth_success(self, api_client, created_user):
        access_token = created_user["access_token"]
        new_email = helpers.generate_unique_email()
        update_data = {"email": new_email}
        
        response = user_methods.update_user(api_client, access_token, update_data)
        
        assert response.json()["user"]["email"] == new_email

    @allure.title("Изменение данных без авторизации - возвращает 401")
    def test_update_user_without_auth_returns_401(self, api_client):
        update_data = {"name": helpers.generate_unique_name()}
        
        url = "https://stellarburgers.education-services.ru/api/auth/user"
        response = api_client.patch(url, json=update_data)
        
        assert response.status_code == 401

    @allure.title("Изменение данных без авторизации - возвращает сообщение об ошибке")
    def test_update_user_without_auth_returns_error_message(self, api_client):
        update_data = {"name": helpers.generate_unique_name()}
        
        url = "https://stellarburgers.education-services.ru/api/auth/user"
        response = api_client.patch(url, json=update_data)
        
        assert response.json()["success"] is False