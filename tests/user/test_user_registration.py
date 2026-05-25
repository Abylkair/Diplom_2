import allure
import data
import helpers
from methods.user_methods import UserMethods

@allure.feature("Создание пользователя")
class TestUserRegistration:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, api_client, unique_user_data):
        email = unique_user_data["email"]
        password = unique_user_data["password"]
        name = unique_user_data["name"]

        response = UserMethods.register_user(api_client, email, password, name)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, api_client, created_user):
        email = created_user["email"]
        password = created_user["password"]
        name = created_user["name"]

        response = UserMethods.register_user(api_client, email, password, name)

        assert response.status_code == 403
        assert response.json()["message"] == data.ERROR_USER_ALREADY_EXISTS

    @allure.title("Создание пользователя без email")
    def test_create_user_without_email(self, api_client):
        password = helpers.generate_unique_password()
        name = helpers.generate_unique_name()

        response = UserMethods.register_user(api_client, "", password, name)

        assert response.status_code == 403
        assert response.json()["message"] == data.ERROR_REQUIRED_FIELDS

    @allure.title("Создание пользователя без пароля")
    def test_create_user_without_password(self, api_client):
        email = helpers.generate_unique_email()
        name = helpers.generate_unique_name()

        response = UserMethods.register_user(api_client, email, "", name)

        assert response.status_code == 403
        assert response.json()["message"] == data.ERROR_REQUIRED_FIELDS

    @allure.title("Создание пользователя без имени")
    def test_create_user_without_name(self, api_client):
        email = helpers.generate_unique_email()
        password = helpers.generate_unique_password()

        response = UserMethods.register_user(api_client, email, password, "")

        assert response.status_code == 403
        assert response.json()["message"] == data.ERROR_REQUIRED_FIELDS