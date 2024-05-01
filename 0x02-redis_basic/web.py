# Imports
import redis
import requests
from functools import wraps

# Redis configuration
redis_client = redis.Redis(host='localhost', port=6379, db=0)


# Decorator for caching and counting
def cache_page(func):
    @wraps(func)
    def wrapper(url):
        # Check cache
        cached = redis_client.get(url)
        if cached:
            redis_client.incr(f'count:{url}')
            return cached.decode()
        else:
            # Fetch and cache the page
            result = func(url)
            redis_client.setex(url, 10, result)
            redis_client.set(f'count:{url}', 1, ex=10)
            return result
    return wrapper


# Main function using the decorator
@cache_page
def get_page(url: str) -> str:
    """Fetch HTML content of the specified URL and cache it."""
    response = requests.get(url)
    return response.text
