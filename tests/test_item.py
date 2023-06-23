"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_init():
    test = Item("1", 2, 3)
    assert test.name == "1"
    assert test.price == 2
    assert test.quantity == 3
    assert len(Item.all) == 1


def test_calculate_total_price():
    test = Item("1", 2, 3)
    assert test.calculate_total_price() == 6


def test_apply_discount():
    test = Item("1", 2, 3)
    test.apply_discount()
    assert test.price == 2

    test.pay_rate = 0.8
    test.apply_discount()
    assert test.price == 1.6
