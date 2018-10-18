class CounterGetter:
    _count = 0

    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        CounterGetter._count += 1
        return value

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        CounterGetter._count += 1

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
    c.b = 5
    print(c.get_count())
