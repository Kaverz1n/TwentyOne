import pytest

from src.player import Player

@pytest.fixture
def fixture_player():
    player = Player("TEST")
    player.cards_have = ["Туз", "Валет", "Дама"]
    player.card_score = 16
    return player


def test_get_last_card(fixture_player):
    player = fixture_player
    assert player.get_last_card() == "Дама"

def test_get_cards(fixture_player):
    player = fixture_player
    assert player.get_cards() == ["Туз", "Валет", "Дама"]

def test_get_cards_score(fixture_player):
    player = fixture_player
    assert player.get_cards_score() == 16

def test_clear_cards(fixture_player):
    player = fixture_player
    player.clear_cards()
    assert player.cards_have == []
    assert player.card_score == 0

def test_get_win_scores(fixture_player):
    player = fixture_player
    assert player.get_win_scores() == 0
    player.win()
    assert player.get_win_scores() == 1

def test_repr(fixture_player):
    player = fixture_player
    assert str(player) == "Игрок TEST"