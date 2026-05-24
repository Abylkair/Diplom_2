import requests
import data

def register_user(session, email, password, name):
    url = data.BASE_URL + data.REGISTER_ENDPOINT
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = session.post(url, json=payload)
    return response


def login_user(session, email, password):
    url = data.BASE_URL + data.LOGIN_ENDPOINT
    payload = {
        "email": email,
        "password": password
    }
    response = session.post(url, json=payload)
    return response


def update_user(session, access_token, update_data):
    url = data.BASE_URL + data.USER_ENDPOINT
    headers = {"Authorization": f"Bearer {access_token}"}
    response = session.patch(url, json=update_data, headers=headers)
    return response


def get_user(session, access_token):
    url = data.BASE_URL + data.USER_ENDPOINT
    headers = {"Authorization": f"Bearer {access_token}"}
    response = session.get(url, headers=headers)
    return response


def logout_user(session, refresh_token):
    url = data.BASE_URL + data.LOGOUT_ENDPOINT
    payload = {"token": refresh_token}
    response = session.post(url, json=payload)
    return response