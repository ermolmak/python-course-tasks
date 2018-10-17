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

    def __repr__(self):
        return f'Vector({", ".join(map(repr, self._storage))})'

    def __str__(self):
        return f'Vector({", ".join(map(str, self._storage))})'

    def __add__(self, other):
        if type(other) != Vector:
            return NotImplemented

        self._check_vector_len(other)
        return Vector(map(lambda x, y: x + y, self._storage, other._storage))

    def __sub__(self, other):
        if type(other) != Vector:
            return NotImplemented

        self._check_vector_len(other)
        return Vector(map(lambda x, y: x - y, self._storage, other._storage))

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
        if not isinstance(other, numbers.Number):
            return NotImplemented
        return Vector(map(lambda x: x / other, self._storage))

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
        if type(matrix) != list or any(map(lambda x: type(x) != list, matrix)):
            raise TypeError('Matrix must be a list of lists')
        new_len = len(matrix[0])
        if len(matrix) != len(self):
            raise ValueError('Matrix height and vector length must be equal')
        if any(map(lambda x: len(x) != new_len, matrix)):
            raise ValueError('All rows in matrix must have the same length')

        res = Vector()
        for i in range(new_len):
            res.push_back(sum(map(lambda x, y: x * matrix[y][i],
                                  self._storage,
                                  range(len(self)))))
        return res


if __name__ == '__main__':
    a = Vector(1, 1.5, -5)
    b = Vector(-4, 0, 3.14)
    c = Vector(1, 2)

    print(a + b)
    # print(a + c)

    print(a - b)

    print(a * b)
    print(a * 2)
    print(2 * a)

    print(a / 2)
    print(len(a), len(b), len(c))
    print(a.matrix_mult([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
