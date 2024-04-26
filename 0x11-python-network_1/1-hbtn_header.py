#!/usr/bin/python3
"""Python script that takes in a URL, sends a request"""
import urllib.request
import sys


if "__main__" == __name__:
    URL = sys.argv
    url_name = URL[1]
    with urllib.request.urlopen(f"{url_name}") as response:
        header = response.getheader('X-Request-Id')
    print(header)
