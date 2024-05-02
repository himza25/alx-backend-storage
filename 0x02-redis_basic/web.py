#!/usr/bin/env python3
"""
Module to implement a simple web page fetcher with caching and access counting
using Redis.
"""
import requests
import redis
from functools import wraps
from typing import Callable

# Create a Redis client instance
_redis = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        count_key = f"count:{url}"
        _redis.incr(count_key)
        return method(*args, **kwargs)
    return wrapper


def cache_page(method: Callable) -> Callable:
    """Decorator to cache the page content."""
    @wraps(method)
    def wrapper(url: str) -> str:
        cache_key = f"cache:{url}"
        cached_content = _redis.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')
        else:
            content = method(url)
            _redis.setex(cache_key, 10, content)
            return content
    return wrapper


@count_requests
@cache_page
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a URL and return it. Keep track of the number of
    times the URL was accessed and cache the content with an expiration time.
    """
    response = requests.get(url)
    return response.text
