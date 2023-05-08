from src.card import Card

CARD = Card("Туз", 11)


def test_get_card_info():
    assert CARD.get_card_info() == "Туз - 11"

def test_get_card_name():
    assert CARD.get_card_name() == "Туз"

def test_get_card_value():
    assert CARD.get_card_value() == 11

def test_repr():
    assert str(CARD) == "Карта Туз со значением 11"