from collections import Generator
from random import randrange


class Agent(Generator):

    def __init__(self, kb, name):
        # Инициализация
        self._texts = kb['text']
        self._name = name

    def __iter__(self):
        return self  # TODO

    def __next__(self):
        return self._texts[randrange(self._texts.size)]  # TODO

    def send(self, msg):
        # Необходимо написать свой собственный метод send для генератора
        return next(self)  # TODO: think about it

    def throw(self, typ=None, val=None, tb=None):
        # Оставляем как есть
        super().throw(typ, val, tb)

    def close(self):
        pass  # TODO

    def __str__(self):
        # Опишем строковое представление класса
        return f'This generator emulates behaviour of "{self._name}"'

    def __repr__(self):
        return str(self)
