from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""
    
    def test_init(self):
        """Тест инициализации базы данных"""
        db = Database()
        
        assert len(db.buns) == 3
        assert db.buns[0].name == "black bun"
        assert db.buns[0].price == 100
        assert db.buns[1].name == "white bun"
        assert db.buns[1].price == 200
        assert db.buns[2].name == "red bun"
        assert db.buns[2].price == 300
        
        assert len(db.ingredients) == 6
        assert db.ingredients[0].name == "hot sauce"
        assert db.ingredients[0].type == INGREDIENT_TYPE_SAUCE
        assert db.ingredients[0].price == 100
        assert db.ingredients[3].name == "cutlet"
        assert db.ingredients[3].type == INGREDIENT_TYPE_FILLING
        assert db.ingredients[3].price == 100
    
    def test_available_buns(self):
        """Тест получения доступных булочек"""
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert buns == db.buns
    
    def test_available_ingredients(self):
        """Тест получения доступных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        assert ingredients == db.ingredients