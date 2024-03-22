#!/usr/bin/env python3
"""
module containing function availableShips
"""
import requests


def availableShips(passengerCount):
    """
    function that returns the list of ships that can hold a given number
        of passengers, using Swapi API
    Args:
        passengerCount: number of passengers
    Return:
        list of ships
    """
    ships = []
    url = 'https://swapi-api.hbtn.io/api/starships/'

    while url:
        res = requests.get(url).json()
        results = res['results']
        for ship in results:
            nb_passengers = ship['passengers'].replace(',', '')
            if nb_passengers not in ['n/a', 'unknown'] and \
               int(nb_passengers) >= passengerCount:
                ships.append(ship['name'])

        url = res['next']

    return ships
