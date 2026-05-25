import allure
import data
from methods.user_methods import UserMethods

@allure.feature("Авторизация пользователя")
class TestUserLogin:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, api_client, created_user):
        email = created_user["email"]
        password = created_user["password"]

        response = UserMethods.login_user(api_client, email, password)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным email")
    def test_login_with_wrong_email(self, api_client, created_user):
        wrong_email = "wrong@test.com"
        password = created_user["password"]

        response = UserMethods.login_user(api_client, wrong_email, password)

        assert response.status_code == 401
        assert response.json()["message"] == data.ERROR_INCORRECT_CREDENTIALS

    @allure.title("Логин с неверным паролем")
    def test_login_with_wrong_password(self, api_client, created_user):
        email = created_user["email"]
        wrong_password = "wrong_password"

        response = UserMethods.login_user(api_client, email, wrong_password)

        assert response.status_code == 401
        assert response.json()["message"] == data.ERROR_INCORRECT_CREDENTIALS