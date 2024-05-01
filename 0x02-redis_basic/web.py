#!/usr/bin/env python3
"""Module for caching and tracking web page accesses using Redis."""

import requests
from redis import Redis
from functools import wraps

# Setup the Redis connection
redis = Redis(host='localhost', port=6379, db=0)


def cache(func):
    """Decorator to cache pages and track page access counts."""
    @wraps(func)
    def wrapper(url: str) -> str:
        """Retrieve web page from cache or fetch and cache it."""
        count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        # Increment the access count
        redis.incr(count_key)

        # Attempt to retrieve the cached content
        cached_content = redis.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # If cache miss, fetch the content and cache it
        page_content = func(url)
        redis.setex(cache_key, 10, page_content)  # Expire after 10 seconds
        return page_content

    return wrapper


@cache
def get_page(url: str) -> str:
    """Fetch HTML content of a URL, caching the results."""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Example URL that simulates a slow response
    slow_url = ("http://slowwly.robertomurray.co.uk/delay/5000/url/"
                "http://www.google.com")
    print(get_page(slow_url))
