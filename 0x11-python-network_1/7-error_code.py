#!/usr/bin/python3
"""Write a Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response.
    """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        data = requests.get(url)
        print(data.text)
    except requests.HTTPError as e:
        print("Error code", e.status_code)
