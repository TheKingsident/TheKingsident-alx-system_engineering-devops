#!/usr/bin/python3
"""
This script defines a function that prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetches titles of all hot articles for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    api_link = f'https://www.reddit.com/r/{subreddit}/hot.json'

    if after:
        api_link += f'?after={after}'

    headers = {'User-Agent': 'Kingsley'}

    response = requests.get(api_link, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    if not response.ok:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after', None)

    for post in posts:
        title = post.get('data', {}).get('title', None)
        if title:
            hot_list.append(title)

    if after is None:
        return hot_list if hot_list else None

    return recurse(subreddit, hot_list, after)
