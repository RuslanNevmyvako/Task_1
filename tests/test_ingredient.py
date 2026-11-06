import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150.5),
        (INGREDIENT_TYPE_SAUCE, "", 200),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 0)
    ])
    def test_ingredient_init(self, ingredient_type, name, price):
        """Тест инициализации ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price
    
    @pytest.mark.parametrize("price", [100, 150.5, 200, 0])
    def test_get_price(self, price):
        """Тест получения цены ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", price)
        assert ingredient.get_price() == price
    
    @pytest.mark.parametrize("name", ["hot sauce", "cutlet", "", "special sauce"])
    def test_get_name(self, name):
        """Тест получения названия ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name
    
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, ingredient_type):
        """Тест получения типа ингредиента"""
        ingredient = Ingredient(ingredient_type, "test", 100)
        assert ingredient.get_type() == ingredient_type