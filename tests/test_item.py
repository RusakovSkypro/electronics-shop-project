"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

def test_init():

    test = Item("1", 2, 3)
    assert test.name == '1'
    assert test.price == 2
    assert test.quantity == 3


def test_calculate_total_price():

    test = Item("1", 2, 3)
    assert test.calculate_total_price() == 6

def test_apply_discount():

    test = Item("1", 2, 3)
    assert test.pay_rate * test.price == 2
    test.pay_rate = 0.8
    assert test.pay_rate * test.price == 1.6
