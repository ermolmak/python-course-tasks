from dialogsgenerator import Agent
from dialogsgenerator import RandomDialog

import sys


def generate(rd, count_dialogs=5):
    """
    Генерирует count_dialogs диалогов с помощью rd.generate().
    Возвращаемый объект является генератором.
    """
    yield from map(lambda i: rd.eval(), range(count_dialogs))


def write(dialogs, target=sys.stdout):
    """
    Записывает сгенерированные диалоги dialogs (это объект-генератор) в поток target.
    """
    print(*map(lambda dialog: f'{f"Dialog {dialog[0]}":_^80}\n' +
                              RandomDialog.dialog_to_str(dialog[1]),
               enumerate(dialogs)), sep='\n', file=target)


if __name__ == "__main__":
    pass
