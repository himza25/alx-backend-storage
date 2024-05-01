#!/usr/bin/env python3
"""
Module to fetch web pages and cache their contents with an expiration time,
also tracks the number of accesses per URL.
"""
import redis
import requests
from functools import wraps
from typing import Callable

# Connect to the Redis server
redis_client = redis.Redis()

def cache_page(expiration: int = 10):
    """
    Decorator to cache web pages and count accesses using Redis.
    Pages are cached with an expiration time.
    """
    def decorator(function: Callable):
        @wraps(function)
        def wrapper(url: str) -> str:
            # Increment access count for the URL
            count_key = f"count:{url}"
            redis_client.incr(count_key)
            
            # Try to retrieve the cached page
            cache_key = f"cache:{url}"
            cached_page = redis_client.get(cache_key)
            if cached_page:
                return cached_page.decode()

            # Fetch the page and cache it
            page_content = function(url)
            redis_client.setex(cache_key, expiration, page_content)
            return page_content
        return wrapper
    return decorator

@cache_page()
def get_page(url: str) -> str:
    """
    Fetch the HTML content of the given URL.
    Decorated to cache its result and track access counts.
    """
    response = requests.get(url)
    return response.text
