import allure
import data
from methods.order_methods import OrderMethods

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth(self, api_client, created_user):
        access_token = created_user["access_token"]
        ingredients = data.VALID_INGREDIENT_IDS

        response = OrderMethods.create_order(api_client, ingredients, access_token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api_client):
        ingredients = data.VALID_INGREDIENT_IDS

        response = OrderMethods.create_order(api_client, ingredients)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, api_client, created_user):
        access_token = created_user["access_token"]
        empty_ingredients = []

        response = OrderMethods.create_order(api_client, empty_ingredients, access_token)

        assert response.status_code == 400
        assert response.json()["message"] == data.ERROR_NO_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self, api_client, created_user):
        access_token = created_user["access_token"]
        invalid_ingredients = [data.INVALID_INGREDIENT_HASH]

        response = OrderMethods.create_order(api_client, invalid_ingredients, access_token)

        assert response.status_code == 500