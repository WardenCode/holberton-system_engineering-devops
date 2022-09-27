#!/usr/bin/python3
"""
Make petitions to the Reddit API
"""

from requests import get


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    base_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit)

    header = {
        'User-Agent': 'Linux:api_advanced:v0.0.0 (by /u/ElEnriquez)'
    }

    response = get(base_url, headers=header, allow_redirects=False)

    if (response.status_code != 200):
        print(None)
        return

    top_ten = response.json().get('data').get('children')

    for topic in top_ten:
        print(topic.get('data').get('title'))
