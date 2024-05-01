#!/usr/bin/env python3
"""
This module provides a Cache class for storing and retrieving data from
Redis, maintaining data types across storage and retrieval operations.
"""
import uuid
import redis
from typing import Union, Callable, Optional


class Cache:
    """Cache class for storing and retrieving data from Redis."""
    def __init__(self):
        """Initialize a Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis by key. If fn is provided, use it to
        process the data before returning; otherwise, return as bytes.
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
