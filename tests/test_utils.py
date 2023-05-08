import pytest
import src.card
from src.player import Player

from src.utils import *


@pytest.fixture
def players_and_card():
    player = Player("TEST")
    bot = Player("Bot")
    card = load_cards("C:/forpy/TwentyOne/files/json_files/card.json")
    return (player, bot, card)


def test_load_cards(capsys):
    FILE = "C:/forpy/TwentyOne/files/json_files/card.json"
    assert type(load_cards(FILE)) is list
    assert type(load_cards(FILE)[0]) is src.card.Card
    assert str(load_cards(FILE)[0]) == "Карта Шестёрка Пики со значением 6"
    load_cards("NOT_FILE_LOC")
    captured = capsys.readouterr()
    assert captured.out == "Файл не найден\n"


@pytest.mark.parametrize('name, rhyme', [
    ("Олежка", "Пельмешка"),
    ("Дима", "Попа бабуина"),
    ("Саша", "Каша"),
    ("NOT_A_NAME", "Нубик")
])
def test_get_rythm(name, rhyme):
    assert get_rhyme(name) == rhyme


@pytest.mark.parametrize('num, phrase', [
    (
            1,
            [
                'Может начнём?',
                'Ну комон!',
                'Е-маё, ты скучный!!!',
                'Не хочешь, так и скажи!',
                'АААААААААААААААА',
                'Мне так больно! ОДИНОКО!',
                'Не ну достал, давай играть!'
                'ГАДДЭМ БОЙ! БЫСТРО ИГРАТЬ!'
            ]
    ),
    (
            2,
            [
                "Ну начнём!",
                "Поехали!",
                "ЛЕЕЕРИИИГОУУУУ",
                "Погнали!",
                "Да начнётся адское очко!"
            ]
    ),
    (
            3,
            [
                "Ну так себе карта!",
                "Неплохо!",
                "Вау!",
                "Да ладно!",
                "Ну не всё потеряно!!",
                "Твою ма..."
            ]
    ),
    (
            4,
            [
                "ИЗИ ПИЗИ ЛЕМОН СКВИЗИ!",
                "Ну сегодня тебе не везёт, друг!",
                "Эх...Мне так...РАДОСТНО ЗА СЕБЯ",
                'В следующий раз ...проиграешь еще раз)))',
                'Ну я харош!',
                'Я МАШИНА!',
                'Изи!',
                'Неплохо',
                'Может повторим?'
            ]
    ),
    (
            5,
            [
                'Да это звездёжь!',
                'Чёрт...как так...как так?!',
                'Тебе просто повезло!',
                'Рукова засучи!',
                'Ну ничего, я отыграюсь',
                'Обыграл машину? Да ты сам этот код и написал!',
                'Е... пироги'
            ],
    ),
])
def test_get_phrase(num, phrase):
    assert get_phrase(num) in phrase


def test_get_rule(capsys):
    RULE_LOC = 'C:/forpy/TwentyOne/files/text_files/rules.txt'
    assert type(get_rules(RULE_LOC)) is str
    get_rules("NOT_FILE_LOC")
    output = capsys.readouterr()
    assert output.out == "Ошибка загрузки правил игры\n"


def test_take_card(players_and_card):
    player, bot, card = players_and_card
    take_card(player, card)
    assert player.get_cards() == ['Туз Черви']
    assert player.get_cards_score() == 11


def test_player_info(players_and_card, capsys):
    player, bot, card = players_and_card
    player.add_card(card[-3].get_card_name())
    player_info(player)
    output = capsys.readouterr()
    print(output)
    assert output.out == '\nВам досталась Туз Бубны\nВсе карты: \x1b[34mТуз Бубны\x1b[39m\nОбщий счёт: \x1b[93m0\n\n'


def test_check_ace(players_and_card):
    player, bot, card = players_and_card
    for i in range(1, 3):
        player.add_card(card[-i].get_card_name())
        player.add_to_card_score(card[-i].get_card_value())
    check_ace(player)
    assert player.get_cards_score() == 21


@pytest.mark.parametrize('player_score, bot_score, winner', [
    (19, 17, True),
    (18, 19, False),
    (21, 21, True),
    (23, 19, False),
    (24, 29, True),
    (12, 25, True)
])
def test_check_round_winner_player(player_score, bot_score, winner, players_and_card):
    player, bot, card = players_and_card
    player.card_score = player_score
    bot.card_score = bot_score
    check_round_winner(player, bot)
    assert player.winner == winner


@pytest.mark.parametrize('player_score, bot_score, winner', [
    (19, 17, False),
    (18, 19, True),
    (21, 21, True),
    (23, 19, True),
    (24, 29, False),
    (23, 22, True)
])
def test_check_round_winner_bot(player_score, bot_score, winner, players_and_card):
    player, bot, card = players_and_card
    player.card_score = player_score
    bot.card_score = bot_score
    check_round_winner(player, bot)
    assert bot.winner == winner

