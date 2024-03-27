#!/usr/bin/env python3
"""
script that displays the number of launches per rocket,
using the (unofficial) SpaceX API
"""
import requests


if __name__ == '__main__':

    url_launch = 'https://api.spacexdata.com/v4/launches'
    url_rocket = 'https://api.spacexdata.com/v4/rockets'
    res_launch = requests.get(url_launch).json()
    res_rocket = requests.get(url_rocket).json()

    rockets = {}

    for launch in res_launch:
        rocket_id = launch['rocket']

        for rocket in res_rocket:
            if rocket['id'] == rocket_id:
                rocket_name = rocket['name']

        if rocket_name in rockets:
            rockets[rocket_name] += 1
        else:
            rockets[rocket_name] = 1

    rockets = sorted(rockets.items(),
                     key=lambda x: x[1],
                     reverse=True)

    for rocket, nb_launches in rockets:
        print('{}: {}'.format(rocket, nb_launches))
