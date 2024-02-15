#!/usr/bin/python3
"""
This script defines a function that returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'Kingsident'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
