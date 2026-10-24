import sys
from pathlib import Path

# Добавляем корневую папку проекта в sys.path
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def burger():
    """Пустой бургер для тестов"""
    return Burger()


@pytest.fixture
def bun():
    """Стандартная булочка"""
    return Bun("black bun", 100)


@pytest.fixture
def mock_bun():
    """Мок булочки с дефолтными значениями"""
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = "black bun"
    bun_mock.get_price.return_value = 100
    return bun_mock


@pytest.fixture
def ingredient():
    """Стандартный ингредиент"""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)


@pytest.fixture
def mock_ingredient():
    """Мок ингредиента с дефолтными значениями"""
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_name.return_value = "test ingredient"
    ingredient_mock.get_price.return_value = 50
    ingredient_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient_mock


@pytest.fixture
def database():
    """База данных с дефолтными данными"""
    return Database()