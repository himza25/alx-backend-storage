#!/usr/bin/env python3
"""
Module to cache web pages and track access count with an expiring cache.
"""
import redis
import requests
from functools import wraps


# Redis client setup
r = redis.Redis()


def count_accesses(func):
    """Decorator to count accesses for a given URL."""
    @wraps(func)
    def wrapper(url):
        # Increment access count for the URL
        count_key = f"count:{url}"
        r.incr(count_key)
        return func(url)
    return wrapper


def cache_page(func):
    """Decorator to cache the webpage content."""
    @wraps(func)
    def wrapper(url):
        # Check if the page is already cached
        cache_key = f"cache:{url}"
        cached_page = r.get(cache_key)
        if cached_page is not None:
            return cached_page.decode()

        # If not cached, fetch the page and cache it
        page_content = func(url)
        r.setex(cache_key, 10, page_content)
        return page_content
    return wrapper


@count_accesses
@cache_page
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and cache it with an expiration."""
    response = requests.get(url)
    return response.text
