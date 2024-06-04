#!/usr/bin/python3
"""Module fires a request to Reddit API and returns the number of subscribers"""
import requests
import sys
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
}
argv = sys.argv[1]


def number_of_subscribers(subreddit):
    """Function returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
