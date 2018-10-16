import math
import numbers


class Vector(object):
    def __init__(self, *args):
        if len(args) == 0:
            self._storage = []
        elif len(args) == 1:
            self._storage = list(args[0])
        else:
            self._storage = list(args)

    def __len__(self):
        return len(self._storage)

    def __getitem__(self, item):
        if type(item) == slice:
            return NotImplemented
        else:
            return self._storage[item]

    def __setitem__(self, key, value):
        if type(key) == slice:
            return NotImplemented
        else:
            self._storage[key] = value

    def __add__(self, other):
        if type(other) == Vector:
            if len(other) != len(self):
                raise ValueError("sum operands aren't length equal")
            return Vector(map(lambda x, y: x + y,
                              self._storage,
                              other._storage))

        elif isinstance(other, numbers.Number):
            return Vector(map(lambda x: x + other, self._storage))
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def matrix_mult(self, matrix):
        pass
