#!/usr/bin/python3
"""
    script that takes in and fetches a URL then displays the response header
    X-Request-Id
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
    for header, value in headers.items():
        if header == 'X-Request-Id':
            print(value)
