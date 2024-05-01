#!/usr/bin/env python3
"""
Enhance Cache class with decorators for counting method calls and storing
call histories in Redis.
"""
import uuid
import redis
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs of a method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        # Convert all arguments to strings and store them
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        # Store the output
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    """Cache class for storing and retrieving data from Redis."""
    def __init__(self):
        """Initialize a Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key and return the key.
        Decorated to count calls and store call history.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key. Optionally process with fn.
        """
        data = self._redis.get(key)
        if data is not None and fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis."""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, int)
