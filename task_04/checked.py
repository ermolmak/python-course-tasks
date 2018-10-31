from functools import wraps


def checked(*types: type):
    if not all(map(lambda o: isinstance(o, type), types)):
        raise TypeError("all arguments of 'checked' must be instances of 'type'")

    def checker(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) != len(types):
                raise TypeError('wrong number of arguments')
            if not all(map(isinstance, args, types)):
                raise TypeError('wrong type')
            return func(*args)

        return wrapper

    return checker


if __name__ == '__main__':
    @checked(int, str)
    def f(x, y):
        print('Hello, World!', x, y)


    f(23, 'max')
