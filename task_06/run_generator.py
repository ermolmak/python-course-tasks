import argparse
import sys

import pandas as pd

from dialogsgenerator import Agent
from dialogsgenerator import RandomDialog


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
    parser = argparse.ArgumentParser()
    parser.add_argument('count_dialogs', type=int,
                        help='Amount of dialogs to generate')
    parser.add_argument('max_dialog_len', type=int,
                        help='Maximum amount of turns in each dialog')
    parser.add_argument('-c', '--clinton_kb', help="Clinton's texts")
    parser.add_argument('-t', '--trump_kb', help="Trump's texts")
    args = parser.parse_args()

    clinton_filename = args.clinton_kb
    if clinton_filename is None:
        clinton_filename = 'clinton.csv'
    trump_filename = args.trump_kb
    if trump_filename is None:
        trump_filename = 'trump.csv'

    if args.count_dialogs <= 0:
        raise ValueError("'count_dialogs' must be positive")
    if args.max_dialog_len <= 0:
        raise ValueError("'max_dialog_len' must be positive")

    clinton = pd.read_csv(clinton_filename)
    trump = pd.read_csv(trump_filename)

    rd = RandomDialog([Agent(clinton, 'clinton'), Agent(trump, 'trump')],
                      args.max_dialog_len)

    write(generate(rd, args.count_dialogs))
