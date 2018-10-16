class CounterGetter:
    _count = 0

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            self.__setattr__(name, value)

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        CounterGetter._count += 1
        return value

    @staticmethod
    def get_count():
        return CounterGetter._count


if __name__ == '__main__':
    c = CounterGetter(a=1, x=2)
    print(c.a, c.x)
    try:
        print(c.b)
    except AttributeError:
        pass
    print(c.get_count())
