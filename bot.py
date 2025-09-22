import httpx


not_found = httpx.get('https://httpbin.org/status/404')


not_found.raise_for_status()