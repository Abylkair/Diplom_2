import data

class IngredientMethods:

    @staticmethod
    def get_ingredients(session):
        url = data.BASE_URL + data.INGREDIENTS_ENDPOINT
        response = session.get(url)
        return response