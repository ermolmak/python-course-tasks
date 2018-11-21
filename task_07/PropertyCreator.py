class PropertyCreator(type):
    def __new__(mcs, name, bases, attrs):
        properties = {}

        storage = type('storage', (), {'__getattr__': lambda self, attr: None})

        for key, value in attrs.items():
            if len(key) > 4 and key.startswith(('get_', 'set_', 'del_')):
                current_name = key[4:]
                if current_name not in properties:
                    properties[current_name] = storage()
                if key.startswith('get_'):
                    properties[current_name].getter = value
                elif key.startswith('set_'):
                    properties[current_name].setter = value
                elif key.startswith('del_'):
                    properties[current_name].deleter = value

        new_attrs = {key: property(value.getter, value.setter, value.deleter)
                     for key, value in properties.items()}
        return type.__new__(mcs, name, bases, dict(**attrs, **new_attrs))


if __name__ == '__main__':
    def test_simple():
        class TestPropertyCreator(metaclass=PropertyCreator):
            def __init__(self, lo):
                self.__x = None
                self.lo = lo

            def get_x(self):
                return self.__x

            def set_x(self, value):
                if value < self.lo:
                    raise ValueError(
                        "Value must in condition: {} <= value".format(self.lo))
                self.__x = value

            def del_x(self):
                self.__x = "No more"

        obj = TestPropertyCreator(42)
        assert obj.x is None

        obj.x = 100
        assert obj.x == 100

        try:
            obj.x = 5
            assert False
        except ValueError:
            pass

        del obj.x
        assert obj.x == 'No more'


    def test_with_inheritance():
        class TestPropertyCreator(metaclass=PropertyCreator):
            pass

        class TestPropertyCreatorInheritance(TestPropertyCreator):
            def __init__(self):
                self._secret_list = []

            def get_x(self):
                self._secret_list.append("get")
                return 0

            def set_x(self, value):
                self._secret_list.append("set")

        pass  # TODO


    def test_partially_defined():
        class TestPropertyCreator(metaclass=PropertyCreator):
            def __init__(self):
                self._secret_list = []

            def get_x(self):
                self._secret_list.append("get")
                return 0

            def set_y(self, value):
                self._secret_list.append("set")
                self._y = value

        pass  # TODO


    def test_sanity():
        class TestPropertyCreator(metaclass=PropertyCreator):
            _text = 0

            def get_raw_text(self):
                return self._boo

            def get_text(self):
                return self._text % 2

            def set_text(self, value):
                try:
                    self._text = int(value)
                except ValueError:
                    raise TypeError("unproper value for text: {}".format(value))

        pass  # TODO


    def test_multiple_usages():
        class TestPropertyCreatorA(metaclass=PropertyCreator):
            def get_x(self):
                return 0

        class TestPropertyCreatorB(metaclass=PropertyCreator):
            def get_x(self):
                return 1

        class TestPropertyCreatorC(metaclass=PropertyCreator):
            def set_x(self, value):
                self.value = value + 1

            def get_x(self):
                return self.value

        pass  # TODO


    test_simple()
