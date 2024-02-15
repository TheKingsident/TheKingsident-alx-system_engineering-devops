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
    headers = {'User-Agent': 'RedditPostFetcher/0.1 by Kingsident'}

    response = requests.get(api_link, headers=headers, allow_redirects=False)

    if not response.ok:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        print(None)
        return

    for post in posts:
        title = post.get('data', {}).get('title', None)
        if title:
            print(title)
        else:
            print("Missing title")
