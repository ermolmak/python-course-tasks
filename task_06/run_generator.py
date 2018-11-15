def generate(rd, count_dialogs=5):
    """
    Генерирует count_dialogs диалогов с помощью rd.generate().
    Возвращаемый объект является генератором.
    """
    yield from map(lambda i: rd.eval(), range(count_dialogs))


def write(dialogs, target):
    """
    Записывает сгенерированные диалоги dialogs (это объект-генератор) в поток target.
    """
    pass


if __name__ == "__main__":
    pass
