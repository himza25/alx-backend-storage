#!/usr/bin/env python3
"""
This module implements a web cache and tracker, caching the HTML content
of URLs for 10 seconds and tracking the count of accesses per URL.
"""

import requests
import redis
from functools import wraps


# Create a Redis connection
store = redis.Redis()


def count_url_access(method):
    """Decorator to count URL accesses and cache the HTML content."""
    @wraps(method)
    def wrapper(url):
        count_key = f"count:{url}"
        cached_key = f"cached:{url}"

        # Check if the URL is already cached
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode('utf-8')

        # Fetch the HTML content if not cached
        html = method(url)

        # Increment access count and set cache with expiration
        store.incr(count_key)
        store.set(cached_key, html, ex=10)  # Expires in 10 seconds
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """Fetch and return the HTML content of a given URL."""
    response = requests.get(url)
    return response.text
