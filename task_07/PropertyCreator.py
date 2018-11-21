from typing import Dict, Any, Tuple


class PropertyCreator(type):
    def __init__(cls, name: str, bases: Tuple[type, ...],
                 attrs: Dict[str, Any]):
        new_cls = super().__init__(cls, name, bases, attrs)

        properties = {}

        storage = type('storage', (), {'__getattr__': lambda self, attr: None})

        for key, value in attrs.items():
            if len(key) > 4 and key.startswith(('get_', 'set_', 'del_')):
                current_name = key[4:]
                properties[current_name] = storage()
                if key.startswith('get_'):
                    properties[current_name].getter = value
                elif key.startswith('set_'):
                    properties[current_name].setter = value
                elif key.startswith('del_'):
                    properties[current_name].deleter = value

        for key, value in properties.items():
            new_cls.__dict__[key] = property(value.getter, value.setter,
                                             value.deleter)
