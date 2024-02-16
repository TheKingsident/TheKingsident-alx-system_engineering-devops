#!/usr/bin/python3
"""
Recursive function that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list, after='', counts=None):
    """
    Recursively queries the Reddit API
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_counts = sorted([item for item in
                                counts.items() if item[1] > 0],
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    headers = {'User-Agent': 'Kingsident'}
    api_link = (f'https://www.reddit.com/r/{subreddit}/hot.json'
                f'?limit=100&after={after}')

    response = requests.get(api_link, headers=headers, allow_redirects=False)

    if not response.ok:
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    after = data.get('data', {}).get('after')

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in counts.keys():
            counts[word] += title.split().count(word)

    count_words(subreddit, word_list, after, counts)
