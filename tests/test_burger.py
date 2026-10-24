import pytest
from unittest.mock import Mock, patch
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""

    def test_init(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    @pytest.mark.parametrize("initial_count, index", [
        (3, 0),
        (3, 1),
        (3, 2)
    ])
    def test_remove_ingredient(self, burger, initial_count, index):
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
    def test_move_ingredient(self, burger, index, new_index, initial_count):
        ingredients = [Mock(spec=Ingredient) for _ in range(initial_count)]
        for ing in ingredients:
            burger.add_ingredient(ing)

        burger.move_ingredient(index, new_index)
        assert burger.ingredients[new_index] == ingredients[index]

    def test_get_price_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_price_with_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200

    def test_get_price_with_bun_and_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_price.return_value = 50
        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_price.return_value = 75

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 325

    def test_get_receipt_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_get_receipt_with_bun_only(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        with patch.object(burger, 'get_price', return_value=200):
            receipt = burger.get_receipt()
            expected_receipt = (
                "(==== black bun ====)\n"
                "(==== black bun ====)\n"
                "\n"
                "Price: 200"
            )
            assert receipt == expected_receipt

    def test_get_receipt_with_bun_and_ingredients(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        ingredient1 = Mock(spec=Ingredient)
        ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient1.get_name.return_value = "hot sauce"
        ingredient1.get_price.return_value = 100

        ingredient2 = Mock(spec=Ingredient)
        ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient2.get_name.return_value = "cutlet"
        ingredient2.get_price.return_value = 150

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        with patch.object(burger, 'get_price', return_value=350):
            receipt = burger.get_receipt()
            expected_receipt = (
                "(==== black bun ====)\n"
                "= sauce hot sauce =\n"
                "= filling cutlet =\n"
                "(==== black bun ====)\n"
                "\n"
                "Price: 350"
            )
            assert receipt == expected_receipt