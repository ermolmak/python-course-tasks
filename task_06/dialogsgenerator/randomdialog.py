from collections import Generator
import random
import sys


class RandomDialog(object):

    def __init__(self, agents, max_len=5):
        self._agents = agents
        self._max_len = max_len

    def generate(self):
        """
        Генерирует случайный диалог состоящий из 1-max_len цепочек.
        При генерации вызывает функцию turn.
        Возвращаемый объект является генератором.
        """
        chains_number = random.randrange(self._max_len) + 1
        turn = self.turn

        class DialogGenerator(Generator):
            def __init__(self):
                self._index = -1

            def __next__(self):
                self._index += 1
                if self._index == len(chains_number):
                    raise StopIteration()
                return list(turn())

            def __iter__(self):
                return self

            def send(self, value):
                return next(self)

            def throw(self, typ=None, val=None, tb=None):
                super().throw(typ, val, tb)

            def close(self):
                pass

        return DialogGenerator()

    def turn(self):
        """
        Генерирует одну случайную цепочку следующим образом: выбирается случайный агент.
        Он "говорит" случайное сообщение (msg) из своей Agent.kb (используйте next или send(None)).
        (правила того, как выбирать никак не регулируются, вы можете выбирать случайный твит из Agent.kb никак не учитывая
        переданное msg).
        Это сообщение передается с помощью send (помним, что агент - это объект-генератор).
        Далее получаем ответ от всех агентов и возвращаем (генерируем) их (включая исходное сообщение).
        Возвращаемый объект является генератором.
        """

        speaker_num = random.randrange(len(self._agents))
        speaker = self._agents[speaker_num]
        other_agents = self._agents[:speaker_num] + \
                       self._agents[speaker_num + 1:]
        random.shuffle(other_agents)
        yield next(speaker)
        yield from map(next, other_agents)

    def eval(self, dialog=None):
        """
        Превращает генератор случайного далога (который возвращается в self.generate())
        в список списков (пример использования далее).
        Возвращаемый объект является списком.
        """
        if dialog is None:
            dialog = self.generate()
        return list(dialog)

    def write(self, dialog=None, target=sys.stdout):
        """
        Записывает результат self.eval() в соответствующий поток.
        """
        if dialog is None:
            dialog = self.eval()
        pass  # TODO

    pass
