#!/usr/bin/env python3
"""
script that displays the first launch, using the (unofficial) SpaceX API
Format:
<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)
"""
import requests


if __name__ == '__main__':

    url = 'https://api.spacexdata.com/v3/launches'
    res = requests.get(url).json()

    first_launch = res[0]
    first_date = first_launch['launch_date_unix']

    for launch in res:
        date = launch['launch_date_unix']
        if date < first_date:
            first_date = date
            first_launch = launch

    launch_name = first_launch['mission_name']
    rocket_name = first_launch['rocket']['rocket_name']
    launchpad_name = first_launch['launch_site']['site_name']
    launchpad_locality = first_launch['launch_site']['site_name_long']
    date = first_launch['launch_date_utc']

    print('{} ({}) {} - {} ({})'.format(launch_name,
                                        date,
                                        rocket_name,
                                        launchpad_name,
                                        launchpad_locality))
