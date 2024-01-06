#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        print(content)
    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
