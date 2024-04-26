#!/usr/bin/python3
"""Write a Python script that takes in a URL,
    sends a request to the URL and
    displays the body of the response.
    """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = requests.get(url)

    if data.status_code >= 400:
        print("Error code:", data.status_code)
    else:
        print(data.text)
