#!/usr/bin/env python3
"""
script that prints the location of a specific user, using GitHub API
"""
import requests
import sys
import time


if __name__ == '__main__':

    url = sys.argv[1]
    res = requests.get(url).json()

    # user doesn’t exist
    if requests.get(url).status_code == 404:
        print('Not found')

    # status code is 403
    elif requests.get(url).status_code == 403:
        reset_limit = int(requests.get(url).headers['X-RateLimit-Reset'])
        now = int(time.time())
        reset = int((reset_limit - now) / 60)
        print('Reset in', reset, 'min')

    else:
        print(res['location'])
