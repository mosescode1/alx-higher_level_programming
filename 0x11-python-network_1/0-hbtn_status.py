#!/usr/bin/python3
"""A module for treading in an url
    """
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print("- type:", type(body))
        print("- content:", body)
        print("- utf8 content:", body.decode('utf-8'))
