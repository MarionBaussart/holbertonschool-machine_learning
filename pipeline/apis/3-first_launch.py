#!/usr/bin/env python3
"""
script that displays the first launch, using the (unofficial) SpaceX API
Format:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)
"""
import requests


if __name__ == '__main__':

    url_launch = 'https://api.spacexdata.com/v4/launches/upcoming'
    url_rocket = 'https://api.spacexdata.com/v4/rockets'
    url_launchpad = 'https://api.spacexdata.com/v4/launchpads'
    res_launch = requests.get(url_launch).json()
    res_rocket = requests.get(url_rocket).json()
    res_launchpad = requests.get(url_launchpad).json()

    first_launch = res_launch[0]
    first_date = first_launch['date_unix']
    rocket_id = first_launch['rocket']
    launchpad_id = first_launch['launchpad']

    for launch in res_launch:
        date = launch['date_unix']
        if date < first_date:
            first_date = date
            first_launch = launch
            rocket_id = first_launch['rocket']
            launchpad_id = first_launch['launchpad']

    launch_name = first_launch['name']
    date = first_launch['date_utc']

    for rocket in res_rocket:
        if rocket['id'] == rocket_id:
            rocket_name = rocket['name']

    for launchpad in res_launchpad:
        if launchpad['id'] == launchpad_id:
            launchpad_name = launchpad['name']
            launchpad_locality = launchpad['locality']

    print('{} ({}) {} - {} ({})'.format(launch_name,
                                        date,
                                        rocket_name,
                                        launchpad_name,
                                        launchpad_locality))
