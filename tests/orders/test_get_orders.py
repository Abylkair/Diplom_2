import allure
import data
from methods import order_methods
from methods import user_methods

@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:

    @allure.title("Получение заказов авторизованного пользователя - возвращает 200")
    def test_get_orders_with_auth_returns_200(self, api_client, created_user):
        access_token = created_user["access_token"]
        
        response = order_methods.get_user_orders(api_client, access_token)
        
        assert response.status_code == 200

    @allure.title("Получение заказов авторизованного пользователя - возвращает success true")
    def test_get_orders_with_auth_returns_success_true(self, api_client, created_user):
        access_token = created_user["access_token"]
        
        response = order_methods.get_user_orders(api_client, access_token)
        
        assert response.json()["success"] is True

    @allure.title("Получение заказов авторизованного пользователя - возвращает список заказов")
    def test_get_orders_with_auth_returns_orders_list(self, api_client, created_user):
        access_token = created_user["access_token"]
        
        response = order_methods.get_user_orders(api_client, access_token)
        
        assert "orders" in response.json()

    @allure.title("Получение заказов без авторизации - возвращает 401")
    def test_get_orders_without_auth_returns_401(self, api_client):
        url = data.BASE_URL + data.GET_ORDERS_ENDPOINT
        response = api_client.get(url)
        
        assert response.status_code == 401

    @allure.title("Получение заказов без авторизации - возвращает сообщение об ошибке")
    def test_get_orders_without_auth_returns_error_message(self, api_client):
        url = data.BASE_URL + data.GET_ORDERS_ENDPOINT
        response = api_client.get(url)
        
        assert response.json()["message"] == data.ERROR_UNAUTHORIZED_ORDERS