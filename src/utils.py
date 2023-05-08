import json
import random
import colorama

from time import sleep
from files.python_lists import (
    phrases,
    rhyme
)
from src.card import Card


def load_cards(file_loc):
    '''
    Загруажет список в формате json, содержащий
    все карты и их значения
    :param file_loc: расположение json-файла
    :return: список карт
    '''
    try:
        with open(file_loc, "r", encoding="UTF-8") as file:
            json_data = file.read()
            cards = json.loads(json_data)
            card_lst = []
            for card in cards:
                card_lst.append(Card(card['name'], card['value']))
        return card_lst
    except:
        print("Файл не найден")


def get_rhyme(player_name):
    '''
    Перебирает список имён и рифм, возвращая рифму к именни;
    Если такого имени нет в списки, то дефолтное значение
    :param player_name: имя игрока
    :return: рифма к имени игрока
    '''
    for name in rhyme.rhymes:
        if name['name'] == player_name.title():
            return name['rhyme']
    return 'Нубик'


def get_phrase(phrase_list_num):
    '''
    Возвращает случайную фразу
    :param phrase_list_num: номер фраз из списке фраз
    :return: случайную фразу
    '''
    phrases_lst = phrases.phrases[phrase_list_num - 1]
    random_phrase = random.choice(phrases_lst)
    return random_phrase


def get_rules(file_loc):
    '''
    Возвращает правила игры
    :param file_loc: расположение файла с правилами
    :return: правила игры
    '''
    try:
        rules = ''
        with open(file_loc, 'r', encoding="UTF-8") as file:
            rules_data = file.read()
            for rule in rules_data:
                rules += rule
        return rules
    except:
        print("Ошибка загрузки правил игры")


def take_card(player_name, card_list):
    '''
    Добавляют карту из колоды в инвентарь игрока
    :param player_name: игрок класса Player
    :param card_list: список карт
    '''
    player_name.add_card(card_list[-1].get_card_name())
    player_name.add_to_card_score(card_list[-1].get_card_value())
    card_list.pop()


def player_info(player):
    '''
    Выводит информацию об картах игрока
    :param player: игрок класса Player
    '''
    print(f'\nВам досталась {player.get_last_card()}')
    print(f"Все карты: {colorama.Fore.BLUE}{', '.join(player.get_cards())}{colorama.Fore.RESET}")
    print(f"Общий счёт: {colorama.Fore.LIGHTYELLOW_EX}{player.get_cards_score()}\n")


def check_ace(player):
    '''
    Проверяет наличие 2 тузов
    :param player: игрок класса Player
    '''
    if len(player.get_cards()) == 2 and player.get_cards_score() == 22:
        player.card_score = 21


def check_round_winner(player, bot):
    '''
    Проверяет кто ближе приблизился к числу 21
    :param player: игрок на основе класса Player
    :param bot: бот на основе класса Player
    '''
    player_one = player.get_cards_score()
    player_two = bot.get_cards_score()
    if player_one != player_two:
        if player_one > 21 and player_two > 21:
            if player_one < player_two:
                player.win()
            else:
                bot.win()
        elif player_one <= 21 and player_two <= 21:
            if player_one > player_two:
                player.win()
            else:
                bot.win()
        else:
            if player_one < player_two:
                player.win()
            else:
                bot.win()
    else:
        player.win()
        bot.win()


def print_round_results(player, bot):
    '''
    Выводит результаты раунда
    :param player: игрок класса Player
    :param bot: бот класса Player
    '''
    print("\nСудья: пора подсчитать очки!")
    sleep(2)
    print("Судья: Так, считаю, погоди!")
    sleep(2)
    print("Судья: И победждает....")
    sleep(3)
    check_round_winner(player, bot)
    if player.winner and bot.winner:
        print("\nСудья: НИЧЬЯ\n")
    elif player.winner:
        print(f"\nСудья: Побеждает {colorama.Fore.LIGHTCYAN_EX}{player}")
        print(f"\n{colorama.Fore.GREEN}BOT: {colorama.Fore.RESET}{get_phrase(5)}\n")
    else:
        print(f"\nСудья: Побеждает {colorama.Fore.GREEN}{bot}")
        print(f"\n{colorama.Fore.GREEN}BOT: {colorama.Fore.RESET}{get_phrase(4)}\n")
    print(f"Очки игрока: {colorama.Fore.LIGHTMAGENTA_EX}{player.get_cards_score()}\n{colorama.Fore.RESET}"
          f"Очки бота: {colorama.Fore.LIGHTMAGENTA_EX}{bot.get_cards_score()}{colorama.Fore.RESET}")
    player.winner = False
    bot.winner = False


def print_game_results(player, bot):
    '''
    Выводит результат всей игры
    :param player: игрок класса Player
    :param bot: бот класса Player
    '''
    sleep(2)
    winner = ""
    if player.get_win_scores() > bot.get_win_scores():
        winner = player
    elif player.get_win_scores() == bot.get_win_scores():
        winner = "НИЧЬЯ"
    else:
        winner = bot
    print("\nСудья: И победителем состязания является...")
    sleep(3)
    print(f"Судья: {colorama.Fore.LIGHTBLUE_EX}{winner}{colorama.Fore.RESET}\nСпасибо всем!\n")
    print(f"{colorama.Fore.LIGHTRED_EX}СПАСИБО ЗА ИГРУ!")
