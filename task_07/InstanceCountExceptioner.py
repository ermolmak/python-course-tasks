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
    _default__max_instance_count__ = 1  # singleton

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
        type.__call__(cls, *args, **kwargs)
