#!/usr/bin/env python3
"""
module containing function sentientPlanets
"""
import requests


def sentientPlanets():
    """
    function that returns the list of names of the home planets of all sentient
        species, using Swapi API
    Return:
        list of planets
    """
    planets = []
    url = 'https://swapi-api.hbtn.io/api/species/'

    while url:
        res = requests.get(url).json()
        results = res['results']

        for specie in results:
            if specie['classification'] == 'sentient' or \
               specie['designation'] == 'sentient':

                url_planet = specie['homeworld']
                if url_planet is not None:
                    res_planet = requests.get(url_planet).json()
                    planets.append(res_planet['name'])

        url = res['next']

    return planets
