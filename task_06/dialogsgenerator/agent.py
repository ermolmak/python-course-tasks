from collections import Generator
from random import randrange
from random import shuffle


class Agent(Generator):

    def __init__(self, kb, name):
        # Инициализация
        self._texts = kb['text']
        self._name = name
        self._create_random_queue()

    def _create_random_queue(self):
        queue = list(range(len(self._texts)))
        shuffle(queue)
        self._iter = iter(queue)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return f'{self._name}: {self._texts[next(self._iter)]}'
        except StopIteration:
            self._create_random_queue()
            return f'{self._name}: {self._texts[next(self._iter)]}'

    def send(self, msg):
        # Необходимо написать свой собственный метод send для генератора
        return next(self)

    def throw(self, typ=None, val=None, tb=None):
        # Оставляем как есть
        super().throw(typ, val, tb)

    def close(self):
        pass

    def __str__(self):
        # Опишем строковое представление класса
        return f'This generator emulates behaviour of "{self._name}"'

    def __repr__(self):
        return str(self)
