#!/usr/bin/python3
"""
   Script that takes in and sends a request to a URL and displays the body
   of the response while catching HTTP status codes greater than 400
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code > 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
