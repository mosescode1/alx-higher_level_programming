#!/usr/bin/python3
"""Python script that takes in a URL and an email,
    sends a POST request to the passed URL
    with the email as a parameter
    displays the body of the response (decoded in utf-8)
    """

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # encode email parameter
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")
    # sending Post Resquest
    with urllib.request.urlopen(url, data=data) as response:
        # reading and decode the response body
        ress = response.read().decode('utf-8')
        print(ress)
