import data

def create_order(session, ingredients, access_token=None):
    url = data.BASE_URL + data.CREATE_ORDER_ENDPOINT
    payload = {"ingredients": ingredients}
    
    headers = {}
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    
    response = session.post(url, json=payload, headers=headers)
    return response


def get_user_orders(session, access_token):
    url = data.BASE_URL + data.GET_ORDERS_ENDPOINT
    headers = {"Authorization": f"Bearer {access_token}"}
    response = session.get(url, headers=headers)
    return response


def get_all_orders(session):
    url = data.BASE_URL + data.GET_ALL_ORDERS_ENDPOINT
    response = session.get(url)
    return response