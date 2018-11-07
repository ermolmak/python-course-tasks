class _ContextManager:
    def __init__(self, main_storage):
        self._main_storage = main_storage
        self._new_storage = {}

    def __getitem__(self, item):
        try:
            return self._new_storage[item]
        except KeyError:
            return self._main_storage[item]

    def __setitem__(self, key, value):
        self._new_storage[key] = value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            return False

        for key, value in self._new_storage.items():
            self._main_storage[key] = value
        return True


class Storage:
    def __init__(self, *args, **kwargs):
        self._storage = dict(*args, **kwargs)

    def __len__(self):
        return len(self._storage)

    def __getitem__(self, item):
        return self._storage[item]

    def edit(self):
        return _ContextManager(self._storage)

    def __repr__(self):
        return f'Storage({repr(self._storage)})'

    def __str__(self):
        return f'Storage({str(self._storage)})'


if __name__ == '__main__':
    pass
