class InstanceCountException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

    def __repr__(self):
        return f'InstanceCountException({repr(self.msg)})'


_MAX_INSTANCE_COUNT = '__max_instance_count__'
_INSTANCE_COUNT = '__instance_count__'


class InstanceCountExceptioner(type):
    _default__max_instance_count__ = 1

    def __new__(mcs, name, bases, attrs):
        new_attrs = {_INSTANCE_COUNT: 0}
        if _MAX_INSTANCE_COUNT not in attrs:
            new_attrs[_MAX_INSTANCE_COUNT] = mcs._default__max_instance_count__

        return type.__new__(mcs, name, bases, dict(**attrs, **new_attrs))

    def __call__(cls, *args, **kwargs):
        cnt = getattr(cls, _INSTANCE_COUNT)
        if cnt >= getattr(cls, _MAX_INSTANCE_COUNT):
            raise InstanceCountException(
                'Too many instances of {}'.format(cls.__name__))
        setattr(cls, _INSTANCE_COUNT, cnt + 1)
        return type.__call__(cls, *args, **kwargs)


if __name__ == '__main__':
    class TestInstanceCountExceptionerA(metaclass=InstanceCountExceptioner):
        __max_instance_count__ = 2

        def __init__(self):
            self.a = 1

        def get(self):
            return self.a


    class TestInstanceCountExceptionerB(metaclass=InstanceCountExceptioner):
        __max_instance_count__ = 3

        def __init__(self):
            self.b = 2

        def get(self):
            return self.b


    class TestInstanceCountExceptionerDefaultValue(
        metaclass=InstanceCountExceptioner):
        def __init__(self):
            self.a = 3

        def get(self):
            return self.a


    def test_simple():
        a = TestInstanceCountExceptionerA()
        b = TestInstanceCountExceptionerB()
        c = TestInstanceCountExceptionerDefaultValue()

        assert a.get() == 1 == a.a
        assert b.get() == 2 == b.b
        assert c.get() == 3 == c.a

        print('test_simple passed!')


    def test_create():
        a2 = TestInstanceCountExceptionerA()
        b2 = TestInstanceCountExceptionerB()

        b3 = TestInstanceCountExceptionerB()

        b2.b = 20
        b3.b = 200

        assert b2.b == 20
        assert b3.b == 200

        print('test_create passed!')


    def test_fail_create_a():
        try:
            TestInstanceCountExceptionerA()
            assert False
        except InstanceCountException:
            pass

        print('test_fail_create_a passed!')


    def test_fail_create_b():
        try:
            TestInstanceCountExceptionerB()
            assert False
        except InstanceCountException:
            pass

        print('test_fail_create_b passed!')


    def test_fail_create_default_value():
        try:
            TestInstanceCountExceptionerDefaultValue()
            assert False
        except InstanceCountException:
            pass

        print('test_fail_create_default_value passed!')


    test_simple()
    test_create()
    test_fail_create_a()
    test_fail_create_b()
    test_fail_create_default_value()
