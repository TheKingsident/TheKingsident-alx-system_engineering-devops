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
    api_link = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'SubredditSubscriberCounter/0.1 by Kingsident'}

    response = requests.get(api_link, headers=headers, allow_redirects=False)

    if not response.ok:
        return 0

    data = response.json()
    subscribers = data.get('data', {}).get('subscribers', 0)

    return int(subscribers) if subscribers else 0
