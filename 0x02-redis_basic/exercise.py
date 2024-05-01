#!/usr/bin/env python3
"""
Cache module to interact with Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to manage a Redis connection and store data with random keys.
    """
    def __init__(self):
        """ Initialize a Redis client and flush the database. """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis using a random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
