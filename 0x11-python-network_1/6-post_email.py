#!/usr/bin/python3
"""Write a Python script that takes in a URL and
    an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
    """
import sys
import requests


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]

    email_data = {"email": email}
    data = requests.post(url, data=email_data)
    print(data.text)
