import allure
import data
import helpers
from methods import user_methods

@allure.feature("Создание пользователя")
class TestUserRegistration:

    @allure.title("Создание уникального пользователя - успешный сценарий")
    def test_create_unique_user_success(self, api_client, unique_user_data):
        email = unique_user_data["email"]
        password = unique_user_data["password"]
        name = unique_user_data["name"]
        
        response = user_methods.register_user(api_client, email, password, name)
        
        assert response.status_code == 200

    @allure.title("Создание уникального пользователя - возвращается success true")
    def test_create_unique_user_returns_success_true(self, api_client, unique_user_data):
        email = unique_user_data["email"]
        password = unique_user_data["password"]
        name = unique_user_data["name"]
        
        response = user_methods.register_user(api_client, email, password, name)
        
        assert response.json()["success"] is True

    @allure.title("Создание уникального пользователя - возвращается accessToken")
    def test_create_unique_user_returns_access_token(self, api_client, unique_user_data):
        email = unique_user_data["email"]
        password = unique_user_data["password"]
        name = unique_user_data["name"]
        
        response = user_methods.register_user(api_client, email, password, name)
        
        assert "accessToken" in response.json()

    @allure.title("Создание пользователя, который уже зарегистрирован - возвращает 403")
    def test_create_existing_user_returns_403(self, api_client, created_user):
        email = created_user["email"]
        password = created_user["password"]
        name = created_user["name"]
        
        response = user_methods.register_user(api_client, email, password, name)
        
        assert response.status_code == 403

    @allure.title("Создание существующего пользователя - возвращает сообщение об ошибке")
    def test_create_existing_user_returns_error_message(self, api_client, created_user):
        email = created_user["email"]
        password = created_user["password"]
        name = created_user["name"]
        
        response = user_methods.register_user(api_client, email, password, name)
        
        assert response.json()["message"] == data.ERROR_USER_ALREADY_EXISTS

    @allure.title("Создание пользователя без email - возвращает 403")
    def test_create_user_without_email_returns_403(self, api_client):
        password = helpers.generate_unique_password()
        name = helpers.generate_unique_name()
        
        response = user_methods.register_user(api_client, "", password, name)
        
        assert response.status_code == 403

    @allure.title("Создание пользователя без email - возвращает сообщение об ошибке")
    def test_create_user_without_email_returns_error_message(self, api_client):
        password = helpers.generate_unique_password()
        name = helpers.generate_unique_name()
        
        response = user_methods.register_user(api_client, "", password, name)
        
        assert response.json()["message"] == data.ERROR_REQUIRED_FIELDS

    @allure.title("Создание пользователя без пароля - возвращает 403")
    def test_create_user_without_password_returns_403(self, api_client):
        email = helpers.generate_unique_email()
        name = helpers.generate_unique_name()
        
        response = user_methods.register_user(api_client, email, "", name)
        
        assert response.status_code == 403

    @allure.title("Создание пользователя без имени - возвращает 403")
    def test_create_user_without_name_returns_403(self, api_client):
        email = helpers.generate_unique_email()
        password = helpers.generate_unique_password()
        
        response = user_methods.register_user(api_client, email, password, "")
        
        assert response.status_code == 403