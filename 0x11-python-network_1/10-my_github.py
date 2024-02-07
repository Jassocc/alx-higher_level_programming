#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = (username, password)
    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        user_info = response.json()
        print(user_info['id'])
    except requests.exceptions.HTTPError as e:
        print(None)
