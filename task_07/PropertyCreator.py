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
