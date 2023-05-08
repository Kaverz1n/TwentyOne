class Player:
    '''
    Класс игрок
    '''

    def __init__(self, nickname):
        self.nickname = nickname
        self.cards_have = []
        self.card_score = 0
        self.winner = False
        self.win_score = 0

    def get_last_card(self):
        '''
        Возвращает последнюю взявшую карту
        :return: карту в конце списка
        '''
        return self.cards_have[-1]

    def get_cards(self):
        '''
        Возвращает список имеющих карт
        :return: список карт игрока
        '''
        return self.cards_have

    def get_cards_score(self):
        '''
        Возвращает общий счёт карт
        :return: общий счёт карт
        '''
        return self.card_score

    def add_card(self, card):
        '''
        Добавляет карту в общий список карт
        :param card: объект класса Card
        '''
        self.cards_have.append(card)

    def add_to_card_score(self, value):
        '''
        Добавляет значение карты к общему счёту значений карт
        :param value: значение карты на основе класса Card
        '''
        self.card_score += value

    def win(self):
        '''
        Добавляет победное очко
        '''
        self.winner = True
        self.win_score += 1

    def clear_cards(self):
        '''
        Удаляет имеющиеся карты игрока,
        обнуляя их счёт (функция необходима для
        начала нового раунда или игры)
        :return:
        '''
        self.cards_have = []
        self.card_score = 0

    def get_win_scores(self):
        '''
        Возвращает количество выигранных раундов
        :return: кол-во выигранных раундов
        '''
        return self.win_score

    def __repr__(self):
        return f"Игрок {self.nickname}"
