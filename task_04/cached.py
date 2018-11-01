from functools import wraps
from collections import OrderedDict


def _advanced_hash(x):
    try:
        return hash(x)
    except TypeError:
        return hash((type(x), str(x)))


def cached(max_count=128):
    if type(max_count) != int:
        raise TypeError("'max_count' must be 'int'")
    if max_count <= 0:
        raise ValueError("'must_count' must be positive")

    def cache(func):
        results = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            args_hash = tuple(_advanced_hash(x) for x in args)
            kwargs_hash = tuple((_advanced_hash(x), _advanced_hash(y)) for x, y in kwargs.items())
            final_hash = hash((hash(args_hash), hash(kwargs_hash)))

            if final_hash in results:
                results.move_to_end(final_hash)
                return results[final_hash]
            else:
                func_result = func(*args, **kwargs)
                results[final_hash] = func_result
                if len(results) > max_count:
                    results.popitem(last=False)
                return func_result

        return wrapper

    return cache
