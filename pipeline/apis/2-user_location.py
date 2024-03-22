#!/usr/bin/env python3
"""
script that prints the location of a specific user, using GitHub API
"""
from datetime import datetime
import requests
import sys


if __name__ == '__main__':

    url = sys.argv[1]
    res = requests.get(url).json()

    # user doesn’t exist
    if not res:
        print(res['message'])

    # status code is 403
    elif requests.get(url).status_code == 403:
        reset_limit = int(requests.get(url).headers['X-RateLimit-Limit'])
        now = int(datetime.now().minute)
        reset = reset_limit - now
        print('Reset in ', reset, ' min')

    else:
        print(res['location'])
