#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps
import time

# Redis client setup
store = redis.Redis()


def count_url_access(method):
    """
    Decorator counting how many times a URL is accessed.
    Increments the count each time the URL is fetched.
    """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            print("Returning cached data")
            return cached_data.decode("utf-8")

        # Fetch new data if not cached
        html = method(url)

        # Increment the access count
        count_key = "count:" + url
        count = store.incr(count_key)
        print(f"Access count for {url}: {count}")

        # Cache the new data with expiration
        store.setex(cached_key, 10, html)
        print(f"Data cached for 10 seconds: {cached_key}")

        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """
    Returns HTML content of a URL
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://google.com"
    print(get_page(url))  # Should fetch and cache
    time.sleep(2)         # Wait for 2 seconds
    print(get_page(url))  # Should return cached data
    time.sleep(10)        # Wait to ensure cache expires
    print(get_page(url))  # Should fetch new data as cache is expired
