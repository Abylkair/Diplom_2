import pytest
import requests
import data
import helpers
from methods.user_methods import UserMethods

@pytest.fixture
def api_client():
    session = requests.Session()
    session.base_url = data.BASE_URL
    yield session
    session.close()


@pytest.fixture
def unique_user_data():
    email = helpers.generate_unique_email()
    password = helpers.generate_unique_password()
    name = helpers.generate_unique_name()
    return {
        "email": email,
        "password": password,
        "name": name
    }


@pytest.fixture
def created_user(api_client, unique_user_data):
    response = UserMethods.register_user(
        session=api_client,
        email=unique_user_data["email"],
        password=unique_user_data["password"],
        name=unique_user_data["name"]
    )

    user_data = unique_user_data.copy()
    access_token = None

    if response.status_code == 200:
        access_token = helpers.extract_token_from_response(response)
        user_data["access_token"] = access_token
        user_data["refresh_token"] = helpers.extract_refresh_token_from_response(response)

    yield user_data


@pytest.fixture
def auth_headers(created_user):
    token = created_user.get("access_token")
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}