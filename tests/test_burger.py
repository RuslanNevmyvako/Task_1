import pytest
from unittest.mock import Mock, patch
from bun import Bun
from ingredient import Ingredient
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""
    
    def test_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []
    
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
    
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock(spec=Ingredient)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient
    
    @pytest.mark.parametrize("initial_count, index", [
        (3, 0),
        (3, 1),
        (3, 2)
    ])
    def test_remove_ingredient(self, initial_count, index):
        burger = Burger()
        ingredients = [Mock(spec=Ingredient) for _ in range(initial_count)]
        for ing in ingredients:
            burger.add_ingredient(ing)
        
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == initial_count - 1
        expected_ingredients = [ing for i, ing in enumerate(ingredients) if i != index]
        assert burger.ingredients == expected_ingredients
    
    @pytest.mark.parametrize("index, new_index, initial_count", [
        (0, 2, 3),
        (1, 0, 3),
        (2, 1, 3)
    ])
    def test_move_ingredient(self, index, new_index, initial_count):
        burger = Burger()
        ingredients = [Mock(spec=Ingredient) for _ in range(initial_count)]
        for ing in ingredients:
            burger.add_ingredient(ing)
        
        burger.move_ingredient(index, new_index)
        assert burger.ingredients[new_index] == ingredients[index]
    
    def test_get_price_without_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()
    
    def test_get_price_with_bun_only(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200
    
    def test_get_price_with_bun_and_ingredients(self):
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = 50
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = 75
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        expected_price = 200 + 50 + 75
        assert burger.get_price() == expected_price
    
    def test_get_receipt_without_bun(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()
    
    def test_get_receipt_with_bun_only(self):
        """Тест получения чека с булочкой без ингредиентов"""
        burger = Burger()
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        
        with patch.object(burger, 'get_price', return_value=200):
            receipt = burger.get_receipt()
            # Добавляем пустую строку после нижней булочки
            expected_receipt = (
                "(==== black bun ====)\n"
                "(==== black bun ====)\n"
                "\n"  # ← ВАЖНО: добавляем пустую строку
                "Price: 200"
            )
            assert receipt == expected_receipt
    
    def test_get_receipt_with_bun_and_ingredients(self):
        """Тест получения чека с булочкой и ингредиентами"""
        burger = Burger()
        
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "black bun"
        burger.set_buns(mock_bun)
        
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "hot sauce"
        mock_ingredient1.get_price.return_value = 100
        
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "cutlet"
        mock_ingredient2.get_price.return_value = 150
        
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        
        with patch.object(burger, 'get_price', return_value=350):
            receipt = burger.get_receipt()
            # Добавляем пустую строку после нижней булочки
            expected_receipt = (
                "(==== black bun ====)\n"
                "= sauce hot sauce =\n"
                "= filling cutlet =\n"
                "(==== black bun ====)\n"
                "\n"  # ← ВАЖНО: добавляем пустую строку
                "Price: 350"
            )
            assert receipt == expected_receipt