# Базовый URL сервера
BASE_URL = "https://stellarburgers.education-services.ru/api"

REGISTER_ENDPOINT = "/auth/register"
LOGIN_ENDPOINT = "/auth/login"
USER_ENDPOINT = "/auth/user"
LOGOUT_ENDPOINT = "/auth/logout"
TOKEN_ENDPOINT = "/auth/token"
CREATE_ORDER_ENDPOINT = "/orders"
GET_ORDERS_ENDPOINT = "/orders"
GET_ALL_ORDERS_ENDPOINT = "/orders/all"
INGREDIENTS_ENDPOINT = "/ingredients"
PASSWORD_RESET_ENDPOINT = "/password-reset"
PASSWORD_RESET_RESET_ENDPOINT = "/password-reset/reset"

# Сообщения об ошибках
ERROR_USER_ALREADY_EXISTS = "User already exists"
ERROR_REQUIRED_FIELDS = "Email, password and name are required fields"
ERROR_INCORRECT_CREDENTIALS = "email or password are incorrect"
ERROR_NO_INGREDIENTS = "Ingredient ids must be provided"
ERROR_UNAUTHORIZED_ORDERS = "You should be authorised"

VALID_INGREDIENT_IDS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6f"  
]

INVALID_INGREDIENT_HASH = "invalid_hash_omgifinallydonethis"

AUTH_HEADER_TEMPLATE = "Bearer {token}"