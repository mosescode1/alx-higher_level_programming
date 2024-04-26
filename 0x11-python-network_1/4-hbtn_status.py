#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
    """
import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    data = requests.get(url)
    # print(help(data))
    print("Body response:")
    print("\t- type:", type(data.text))
    print("\t- content:", data.text)
