class Card:
    '''
    Класс игровых карт
    '''

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_card_info(self):
        '''
        Возвращает информацию о карте
        :return: информация о карте
        '''
        return f'{self.name} - {self.value}'

    def get_card_name(self):
        '''
        Возвращает имя карты
        :return: имя карты
        '''
        return self.name

    def get_card_value(self):
        '''
        Возвращает числовое значение карты
        :return: значение карты
        '''
        return self.value

    def __repr__(self):
        return f"Карта {self.name} со значением {self.value}"
