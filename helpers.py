import time
import random

def generate_unique_email():
    timestamp = int(time.time() * 1000)
    random_suffix = random.randint(1000, 9999)
    return f"test_user_{timestamp}_{random_suffix}@yandex.ru"


def generate_unique_name():
    timestamp = int(time.time())
    return f"TestUser{timestamp}"


def generate_unique_password():
    timestamp = int(time.time())
    return f"Password{timestamp}"


def extract_token_from_response(response):
    response_json = response.json()
    access_token = response_json.get("accessToken", "")
    if access_token.startswith("Bearer "):
        access_token = access_token.replace("Bearer ", "")
    return access_token


def extract_refresh_token_from_response(response):
    response_json = response.json()
    return response_json.get("refreshToken", "")