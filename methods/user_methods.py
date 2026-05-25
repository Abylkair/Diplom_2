import data

class UserMethods:

    @staticmethod
    def register_user(session, email, password, name):
        url = data.BASE_URL + data.REGISTER_ENDPOINT
        payload = {"email": email, "password": password, "name": name}
        response = session.post(url, json=payload)
        return response

    @staticmethod
    def login_user(session, email, password):
        url = data.BASE_URL + data.LOGIN_ENDPOINT
        payload = {"email": email, "password": password}
        response = session.post(url, json=payload)
        return response

    @staticmethod
    def update_user(session, access_token, update_data):
        url = data.BASE_URL + data.USER_ENDPOINT
        headers = {"Authorization": f"Bearer {access_token}"}
        response = session.patch(url, json=update_data, headers=headers)
        return response

    @staticmethod
    def get_user(session, access_token):
        url = data.BASE_URL + data.USER_ENDPOINT
        headers = {"Authorization": f"Bearer {access_token}"}
        response = session.get(url, headers=headers)
        return response

    @staticmethod
    def logout_user(session, refresh_token):
        url = data.BASE_URL + data.LOGOUT_ENDPOINT
        payload = {"token": refresh_token}
        response = session.post(url, json=payload)
        return response