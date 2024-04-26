#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
import urllib.request
import sys
URL = sys.argv
url_name = URL[1]

with urllib.request.urlopen(f"{url_name}") as response:
    header = response.getheader('X-Request-Id')
    print(header)
