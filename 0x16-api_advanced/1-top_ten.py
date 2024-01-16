#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests



def top_ten(subreddit):
    """a function that queries the Reddit API"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    headers = {'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/adetule-ayomide)'}

    try:
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        post_data = response.json().get('data', {}).get('children', [])

        for post in post_data[:10]:
            title = post.get('data', {}).get('title', '')
            print(title)

    except requests.RequestException:
        print(None)

