import allure
import data
from methods.order_methods import OrderMethods

@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_with_auth(self, api_client, created_user):
        access_token = created_user["access_token"]

        response = OrderMethods.get_user_orders(api_client, access_token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "orders" in response.json()

    @allure.title("Получение заказов без авторизации")
    def test_get_orders_without_auth(self, api_client):
        url = data.BASE_URL + data.GET_ORDERS_ENDPOINT
        response = api_client.get(url)

        assert response.status_code == 401
        assert response.json()["message"] == data.ERROR_UNAUTHORIZED_ORDERS