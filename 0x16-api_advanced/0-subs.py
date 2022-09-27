#!/usr/bin/python3
"""
Make petitions to the Reddit API
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Takes a subreddit and compute the quantity of subs
    """

    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    header = {
        'User-Agent': 'Linux:api_advanced:v0.0.0 (by /u/ElEnriquez)'
    }

    response = get(base_url, headers=header, allow_redirects=False)

    if (response.status_code != 200):
        return(0)

    data = response.json()
    subs = data.get('data').get('subscribers')

    return (subs)
