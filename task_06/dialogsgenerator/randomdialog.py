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
        yield from map(lambda x: list(self.turn()), range(chains_number))

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

        msg = next(speaker)
        yield msg
        yield from map(lambda agent: agent.send(msg), other_agents)

    def eval(self, dialog=None):
        """
        Превращает генератор случайного далога (который возвращается в self.generate())
        в список списков (пример использования далее).
        Возвращаемый объект является списком.
        """
        if dialog is None:
            dialog = self.generate()
        return list(dialog)

    @staticmethod
    def dialog_to_str(dialog):
        return '\n'.join(map(lambda turn: f'turn {turn[0]}:\n' + '\n'.join(
            map(lambda s: '\t' + s, turn[1])), enumerate(dialog)))

    def write(self, dialog=None, target=sys.stdout):
        """
        Записывает результат self.eval() в соответствующий поток.
        """
        if dialog is None:
            dialog = self.eval()
        print(self.dialog_to_str(dialog), file=target)
