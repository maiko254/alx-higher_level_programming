#!/usr/bin/python3
"""
   Script that takes in and fetches a URL and displays the value of the
   variable X-Request-Id in the response header
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
