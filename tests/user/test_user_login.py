import allure
import data
from methods import user_methods

@allure.feature("Авторизация пользователя")
class TestUserLogin:

    @allure.title("Логин под существующим пользователем - возвращает 200")
    def test_login_existing_user_returns_200(self, api_client, created_user):
        email = created_user["email"]
        password = created_user["password"]
        
        response = user_methods.login_user(api_client, email, password)
        
        assert response.status_code == 200

    @allure.title("Логин под существующим пользователем - возвращает success true")
    def test_login_existing_user_returns_success_true(self, api_client, created_user):
        email = created_user["email"]
        password = created_user["password"]
        
        response = user_methods.login_user(api_client, email, password)
        
        assert response.json()["success"] is True

    @allure.title("Логин под существующим пользователем - возвращает accessToken")
    def test_login_existing_user_returns_access_token(self, api_client, created_user):
        email = created_user["email"]
        password = created_user["password"]
        
        response = user_methods.login_user(api_client, email, password)
        
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным email - возвращает 401")
    def test_login_with_wrong_email_returns_401(self, api_client, created_user):
        wrong_email = "wrong@test.com"
        password = created_user["password"]
        
        response = user_methods.login_user(api_client, wrong_email, password)
        
        assert response.status_code == 401

    @allure.title("Логин с неверным email - возвращает сообщение об ошибке")
    def test_login_with_wrong_email_returns_error_message(self, api_client, created_user):
        wrong_email = "wrong@test.com"
        password = created_user["password"]
        
        response = user_methods.login_user(api_client, wrong_email, password)
        
        assert response.json()["message"] == data.ERROR_INCORRECT_CREDENTIALS

    @allure.title("Логин с неверным паролем - возвращает 401")
    def test_login_with_wrong_password_returns_401(self, api_client, created_user):
        email = created_user["email"]
        wrong_password = "wrong_password"
        
        response = user_methods.login_user(api_client, email, wrong_password)
        
        assert response.status_code == 401

    @allure.title("Логин с неверным паролем - возвращает сообщение об ошибке")
    def test_login_with_wrong_password_returns_error_message(self, api_client, created_user):
        email = created_user["email"]
        wrong_password = "wrong_password"
        
        response = user_methods.login_user(api_client, email, wrong_password)
        
        assert response.json()["message"] == data.ERROR_INCORRECT_CREDENTIALS