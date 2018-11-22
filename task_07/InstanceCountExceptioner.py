class InstanceCountException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return f'InstanceCountException: {self.msg}'

    def __repr__(self):
        return f'InstanceCountException({repr(self.msg)})'
