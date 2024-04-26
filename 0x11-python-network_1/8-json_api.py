#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends
    POST request to http://0.0.0.0:5000/search_user with
    the letter as a parameter.
    """

import sys
import requests

if __name__ == "__main__":

    alpha = ""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        alpha = sys.argv[1]

    param = {'q': alpha}

    try:
        response = requests.post(url, data=param)
        value = response.json()

        if value:
            print(f"[{value.get("id")}] {value.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
