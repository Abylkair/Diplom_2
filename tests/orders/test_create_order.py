import allure
import data
from methods import order_methods

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами - возвращает 200")
    def test_create_order_with_auth_and_ingredients_returns_200(
        self, api_client, created_user, valid_ingredients
    ):
        access_token = created_user["access_token"]
        
        response = order_methods.create_order(
            api_client, valid_ingredients, access_token
        )
        
        assert response.status_code == 200

    @allure.title("Создание заказа с авторизацией и ингредиентами - возвращает success true")
    def test_create_order_with_auth_and_ingredients_returns_success_true(
        self, api_client, created_user, valid_ingredients
    ):
        access_token = created_user["access_token"]
        
        response = order_methods.create_order(
            api_client, valid_ingredients, access_token
        )
        
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации но с ингредиентами - возвращает 200")
    def test_create_order_without_auth_returns_200(self, api_client, valid_ingredients):
        response = order_methods.create_order(api_client, valid_ingredients)
        
        assert response.status_code == 200

    @allure.title("Создание заказа без авторизации но с ингредиентами - возвращает success true")
    def test_create_order_without_auth_returns_success_true(self, api_client, valid_ingredients):
        response = order_methods.create_order(api_client, valid_ingredients)
        
        assert response.json()["success"] is True

    @allure.title("Создание заказа с авторизацией без ингредиентов - возвращает 400")
    def test_create_order_with_auth_no_ingredients_returns_400(
        self, api_client, created_user
    ):
        access_token = created_user["access_token"]
        empty_ingredients = []
        
        response = order_methods.create_order(api_client, empty_ingredients, access_token)
        
        assert response.status_code == 400

    @allure.title("Создание заказа с авторизацией без ингредиентов - возвращает сообщение")
    def test_create_order_with_auth_no_ingredients_returns_error_message(
        self, api_client, created_user
    ):
        access_token = created_user["access_token"]
        empty_ingredients = []
        
        response = order_methods.create_order(api_client, empty_ingredients, access_token)
        
        assert response.json()["message"] == data.ERROR_NO_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиентов - возвращает 500")
    def test_create_order_with_invalid_ingredient_hash_returns_500(
        self, api_client, created_user
    ):
        access_token = created_user["access_token"]
        invalid_ingredients = [data.INVALID_INGREDIENT_HASH]
        
        response = order_methods.create_order(api_client, invalid_ingredients, access_token)
        
        assert response.status_code == 500