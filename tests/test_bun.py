import pytest
from bun import Bun


class TestBun:
    """Тесты для класса Bun"""
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 0),
        ("", 150)
    ])
    def test_bun_init(self, name, price):
        """Тест инициализации булочки с разными параметрами"""
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 0)
    ])
    def test_get_name(self, name, price):
        """Тест получения названия булочки"""
        bun = Bun(name, price)
        assert bun.get_name() == name
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 0)
    ])
    def test_get_price(self, name, price):
        """Тест получения цены булочки"""
        bun = Bun(name, price)
        assert bun.get_price() == price