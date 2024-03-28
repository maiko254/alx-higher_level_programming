#!/usr/bin/python3
"""
   Script that takes in a URL and a letter, sends a POST request to the URL
   with letter as parameter and displays id and name if response body is JSON
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        letter = argv[1]
    else:
        letter = ""

    r = requests.post(url, data={'q': letter})
    try:
        json_res = r.json()
        if json_res:
            print(f"[{json_res['id']}] {json_res['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
