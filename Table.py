class Table:
    class _Column:
        def __init__(self, iterable, name=None):
            self._storage = list(iterable)
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if type(value) != str and value is not None:
                raise TypeError("columns name must be 'str' or None")
            self._name = value

        def __len__(self):
            return len(self._storage)

        def __getitem__(self, item):
            return self._storage[item]

        def __setitem__(self, key, value):
            self._storage[key] = value

    @staticmethod
    def _col_iter(table, col):
        for i in range(len(table)):
            try:
                yield table[i][col]
            except IndexError:
                yield None

    def __init__(self, table):
        if type(table) != list or any(map(lambda x: type(x) != list, table)):
            raise TypeError('initializer must be a list of lists')

        col_num = max(map(len, table), default=0)
        self._columns = []
        for i in range(col_num):
            self._columns.append(Table._Column(Table._col_iter(table, i)))

        self._names = {}

    def __len__(self):
        return len(self._columns)

    def set_name(self, index, name):
        if name in self._names:
            raise ValueError(f'"{name}" column already exists')

        old_name = self._columns[index].name
        self._columns[index].name = name

        if old_name is not None:
            del self._names[old_name]
        if name is not None:
            self._names[name] = index

    def __getitem__(self, item):
        if type(item) == str:
            return self._columns[self._names[item]]
        elif type(item) == int:
            return self._columns[item]

    def head(self, count):
        res = Table([])

        for col in self._columns:
            res._columns.append(Table._Column(col[:count], name=col.name))

        res._names = self._names

    def tail(self, count):
        res = Table([])

        for col in self._columns:
            res._columns.append(Table._Column(col[-count:], name=col.name))

        res._names = self._names

    @staticmethod
    def read(file, titles=False, sep=','):
        names = []
        if titles:
            names = file.readline().split(sep)
        data = []
        for line in file:
            data.append(line.split(sep))

        res = Table(data)

        if titles:
            for i in range(min(len(res), len(names))):
                res.set_name(i, names[i])
