from functools import wraps
from typing import Callable, Iterable


def listen(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Iterable:
        while True:
            for event in func(*args, **kwargs):
                yield event
    return wrapper
