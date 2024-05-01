#!/usr/bin/env python3
"""
This module provides a Cache class for interacting with a Redis database.
Methods allow for storing data, retrieving data,
incrementing method call counts,
storing call histories, and replaying the history of calls.
"""
import redis
import uuid
from typing import Union, Callable, TypeVar
from functools import wraps

# Define a type alias for the return type to clean up annotations
RedisValue = Union[str, bytes, int, float, None]


class Cache:
    """
    Cache class for managing storage and retrieval of data in Redis.
    """
    def __init__(self):
        """
        Initialize Redis connection and flush the database to start clean.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a UUID. Returns the storage key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> RedisValue:
        """
        Retrieve data by key. Optionally apply a function `fn` to convert
        the data to the desired format.
        """
        value = self._redis.get(key)
        if value is not None and fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Retrieve a string value from Redis. """
        return self.get(key, fn=lambda x: x.decode())

    def get_int(self, key: str) -> int:
        """ Retrieve an integer value from Redis. """
        return self.get(key, fn=int)


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to record the history of arguments and return values.
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(input_key, str(args))
        result = method(self, *args)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """
    Function to display the history of calls of a method.
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    inputs = method._redis.lrange(input_key, 0, -1)
    outputs = method._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{inp.decode()}) -> {out.decode()}")


if __name__ == "__main__":
    cache = Cache()
    key = cache.store("example data")
    print(key)
    print(cache.get(key))
    replay(cache.store)
