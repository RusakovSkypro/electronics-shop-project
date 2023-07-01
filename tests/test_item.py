"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_init():
    test = Item("1", 2, 3)
    # assert test.__name == "1"
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


def test_string_to_number():
    assert Item.string_to_number('rere4545') == 4545
    assert Item.string_to_number('312312----9') == 3123129

# def test_instantiate_from_csv():
#     assert len(Item.instantiate_from_csv()) == 3
