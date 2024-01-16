#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/adetule-ayomide)'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        subreddit_data = response.json().get('data', {})
        subscribers_count = subreddit_data.get('subscribers', 0)
        return subscribers_count
    elif response.status_code == 404:
        print(f"The subreddit '{subreddit}' is not valid.")
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0
