class InstanceCountException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return f'InstanceCountException: {self.msg}'

    def __repr__(self):
        return f'InstanceCountException({repr(self.msg)})'


_MAX_INSTANCE_COUNT = '__max_instance_count__'
_INSTANCE_COUNT = '__instance_count__'


class InstanceCountExceptioner(type):
    _default__max_instance_count__ = 1  # singleton

    def __new__(mcs, name, bases, attrs):
        new_attrs = {_INSTANCE_COUNT: 0}
        if _MAX_INSTANCE_COUNT not in attrs:
            new_attrs[_MAX_INSTANCE_COUNT] = mcs._default__max_instance_count__

        return type.__new__(mcs, name, bases, dict(**attrs, **new_attrs))

    def __call__(cls, *args, **kwargs):
        if cls.__getattribute__(_INSTANCE_COUNT) >= \
                cls.__getattribute__(_MAX_INSTANCE_COUNT):
            raise InstanceCountException(
                f'Too many instances of {cls.__name__}')
        type.__call__(cls, *args, **kwargs)
