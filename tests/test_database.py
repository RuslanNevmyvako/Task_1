from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def test_init(self, database):
        """Тест инициализации базы данных"""
        assert len(database.buns) == 3
        assert database.buns[0].name == "black bun"
        assert database.buns[0].price == 100
        assert database.buns[1].name == "white bun"
        assert database.buns[1].price == 200
        assert database.buns[2].name == "red bun"
        assert database.buns[2].price == 300

        assert len(database.ingredients) == 6
        assert database.ingredients[0].name == "hot sauce"
        assert database.ingredients[0].type == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[0].price == 100
        assert database.ingredients[3].name == "cutlet"
        assert database.ingredients[3].type == INGREDIENT_TYPE_FILLING
        assert database.ingredients[3].price == 100

    def test_available_buns(self, database):
        """Тест получения доступных булочек"""
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns == database.buns

    def test_available_ingredients(self, database):
        """Тест получения доступных ингредиентов"""
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients == database.ingredients