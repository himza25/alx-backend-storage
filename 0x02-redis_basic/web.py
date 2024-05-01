#!/usr/bin/env python3

import redis
import requests
from functools import wraps


def cache_decorator(ttl: int = 10):
    """
    A decorator to cache the result of a function with an expiration time.

    Args:
        ttl (int): The time to live in seconds.

    Returns:
        A decorator function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(url: str) -> str:
            redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
            cache_key = f"cache:{url}"
            count_key = f"count:{url}"
            if redis_client.exists(cache_key):
                return redis_client.get(cache_key).decode('utf-8')
            else:
                result = func(url)
                redis_client.setex(cache_key, ttl, result)
                redis_client.incr(count_key)
                return result
        return wrapper
    return decorator


@cache_decorator(ttl=10)
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL.

    Args:
        url (str): The URL to retrieve.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
