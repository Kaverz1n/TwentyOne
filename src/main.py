from player import Player
from utils import *

import random
import colorama

BOT_NAME = 'BOT'
CARDS = load_cards('../files/json_files/card.json')
RULES = get_rules('../files/text_files/rules.txt')


def main():
    colorama.init()
    player_name = input(colorama.Style.BRIGHT + "Привет, друг, как к тебе обращаться?\nВас зовут: ")

    player = Player(player_name)
    bot = Player(BOT_NAME)

    print(colorama.Fore.GREEN + f"\n{BOT_NAME}: " + colorama.Fore.RESET +
          f"Ну, привет, {get_rhyme(player_name)}, стоп, точнее {player_name}\n"
          f"Сорян перегнул!")
    print(colorama.Fore.GREEN + f"\n{BOT_NAME}: " + colorama.Fore.RESET +
          f"Меня зовут {BOT_NAME} и я буду играть против тебя\n")

    while True:
        user_answer = input("Готов? (y\\n) ")
        if user_answer.strip().lower() == 'y':
            break
        else:
            print(colorama.Fore.GREEN + f"{BOT_NAME}:{colorama.Fore.RESET} {get_phrase(1)}")

    print(colorama.Fore.GREEN + f"{BOT_NAME}:{colorama.Fore.RESET} {get_phrase(2)}")
    print(RULES)

    for round in range(3):
        player.clear_cards()
        bot.clear_cards()
        deck = CARDS.copy()
        random.shuffle(deck)

        while True:
            print(f"\n{colorama.Fore.CYAN}В колоде {len(deck)} карт!{colorama.Fore.RESET}")
            if len(deck) == 0:
                break
            take_input = input("Взять карту? (y\\n) ")
            if take_input == "y":
                take_card(player, deck)
                print(f"{colorama.Fore.GREEN}\n{BOT_NAME}:{colorama.Fore.RESET} {get_phrase(3)}")
                check_ace(player)
                player_info(player)

                if bot.card_score < 17:
                    take_card(bot, deck)
                    check_ace(bot)
                    print(f"{colorama.Fore.LIGHTYELLOW_EX}{BOT_NAME} взял карту!{colorama.Fore.RESET}")

            elif take_input == "n":
                while bot.card_score < 17:
                    print(f"{colorama.Fore.CYAN}В колоде {len(deck)} карт!{colorama.Fore.RESET}")
                    print(f"{colorama.Fore.LIGHTYELLOW_EX}{BOT_NAME} взял карту!{colorama.Fore.RESET}")
                    sleep(2)
                    take_card(bot, deck)
                    check_ace(bot)
                break
            else:
                print(colorama.Fore.GREEN + f"{BOT_NAME}:{colorama.Fore.RESET} Не понял чёт")
        print_round_results(player, bot)
    print_game_results(player, bot)

if __name__ == '__main__':
    main()
