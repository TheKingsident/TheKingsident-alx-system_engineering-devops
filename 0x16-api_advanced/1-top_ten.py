#!/usr/bin/python3
"""
This script defines a function that prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    """
    api_link = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {'User-Agent': 'Kingsident'}

    try:
        response = requests.get(api_link, headers=headers,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(f"Error: {e}")
        print(None)
