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
            self._check_vector_len(other)
            return Vector(map(lambda x, y: x + y,
                              self._storage,
                              other._storage))

        elif isinstance(other, numbers.Number):
            return Vector(map(lambda x: x + other, self._storage))
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == Vector:
            self._check_vector_len(other)
            return Vector(map(lambda x, y: x - y,
                              self._storage,
                              other._storage))
        elif isinstance(other, numbers.Number):
            return Vector(map(lambda x: x - other, self._storage))
        else:
            return NotImplemented

    def __rsub__(self, other):
        if type(other) == Vector:
            self._check_vector_len(other)
            return Vector(map(lambda x, y: x - y,
                              other._storage,
                              self._storage))
        elif isinstance(other, numbers.Number):
            return Vector(map(lambda x: other - x, self._storage))
        else:
            return NotImplemented

    def __mul__(self, other):
        if type(other) == Vector:
            self._check_vector_len(other)
            return sum(map(lambda x, y: x * y, self._storage, other._storage))
        elif isinstance(other, numbers.Number):
            return Vector(map(lambda x: x * other, self._storage))
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return Vector(map(lambda x: x / other, self._storage))
        return NotImplemented

    def _check_vector_len(self, other):
        if len(other) != len(self):
            raise ValueError("operand Vectors aren't length equal")

    def push_back(self, value):
        self._storage.append(value)

    def pop_back(self):
        value = self._storage[-1]
        del self._storage[-1]
        return value

    def insert(self, pos, value):
        self._storage.insert(pos, value)

    def matrix_mult(self, matrix):
        pass
