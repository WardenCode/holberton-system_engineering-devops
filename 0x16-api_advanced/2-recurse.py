#!/usr/bin/python3
"""
Make recursive petitions to the Reddit API
"""

from requests import get


header = {
    'User-Agent': 'Linux:api_advanced:v0.0.0 (by /u/ElEnriquez)'
}


def recurse(subreddit, hot_list=[]):
    """
    Prints the titles of the hot posts listed for a given subreddit.
    recursively
    """

    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = get(base_url, headers=header, allow_redirects=False)

    if (response.status_code != 200):
        return (None)

    size_list = len(hot_list)

    data = response.json().get('data')
    elements = data.get('children')

    if (size_list != len(elements)):
        title = elements[size_list].get('data').get('title')
        hot_list.append(title)
        recurse(subreddit, hot_list)

    return (hot_list)
