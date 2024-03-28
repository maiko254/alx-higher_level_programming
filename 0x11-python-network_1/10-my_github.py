#!/usr/bin/python3
"""
   takes your GitHub credentials and uses the GitHub API to display your id
"""
import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    json_data = response.json()
    print(json_data.get("id"))
