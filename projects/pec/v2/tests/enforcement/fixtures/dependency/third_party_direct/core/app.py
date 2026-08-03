import requests


def fetch() -> object:
    return requests.get("https://example.invalid")
