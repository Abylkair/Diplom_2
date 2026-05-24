import data

def get_ingredients(session):
    url = data.BASE_URL + data.INGREDIENTS_ENDPOINT
    response = session.get(url)
    return response