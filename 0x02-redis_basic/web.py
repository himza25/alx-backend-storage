#!/usr/bin/env python3
"""
Module for caching and tracking web page accesses using Redis.
Implements a decorator to handle caching and count tracking.
"""

import requests
from redis import Redis
from functools import wraps


# Setup the Redis connection
redis = Redis(host='localhost', port=6379, db=0)


def cache(func):
    """
    Decorate a function to cache its web responses and track access counts.
    Each accessed URL has its content cached and access count incremented.
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        """
        Wrapper function to manage caching. If the requested URL is in the
        cache, return the cached content, otherwise fetch, cache, and return.
        """
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        # Increment the access count for the URL
        redis.incr(count_key)

        # Check if the URL is already cached
        cached_content = redis.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch, cache, and return the content if not cached
        page_content = func(url)
        redis.setex(cache_key, 10, page_content)
        return page_content

    return wrapper


@cache
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL. This function is decorated to use Redis
    for caching the content and tracking how many times a URL has been accessed
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Test the function with a URL that simulates a slow response
    slow_url = ("http://slowwly.robertomurray.co.uk/delay/5000/url/"
                "http://www.google.com")
    print(get_page(slow_url))
