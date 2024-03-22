# Data Collection - APIs
- How to use the Python package ``requests``
- How to make HTTP ``GET`` request
- How to handle rate limit
- How to handle pagination
- How to fetch JSON resources
- How to manipulate data from an external service

## 0. Can I join?
By using the [Swapi API](https://swapi-api.hbtn.io/), create a method that returns the list of ships that can hold a given number of passengers:

- Prototype: ``def availableShips(passengerCount):``
- Don’t forget the pagination
- If no ship available, return an empty list.

## 1. Where I am?
By using the [Swapi API](https://swapi-api.hbtn.io/), create a method that returns the list of names of the home planets of all ``sentient`` species.

- Prototype: ``def sentientPlanets():``
- Don’t forget the pagination
- ``sentient`` type is either in the ``classification`` or ``designation`` attributes.

## 2. Rate me is you can!
By using the [GitHub API](https://intranet.hbtn.io/rltoken/xdgGEjSlP0LhW9VUYrbZwQ), write a script that prints the location of a specific user:

- The user is passed as first argument of the script with the full API URL, example: ``./2-user_location.py https://api.github.com/users/holbertonschool``
- If the user doesn’t exist, print ``Not found``
- If the status code is ``403``, print ``Reset in X min`` where ``X`` is the number of minutes from now and the value of ``X-Ratelimit-Reset``
- Your code should not be executed when the file is imported (you should use ``if __name__ == '__main__':``)

## 3. First launch
By using the [(unofficial) SpaceX API](https://intranet.hbtn.io/rltoken/9ZUsU3hvyeVYwax_R2XTKA), write a script that displays the first launch with these information:

- Name of the launch
- The date (in local time)
- The rocket name
- The name (with the locality) of the launchpad
Format: ``<launch name> (<date>) <rocket name> - <launchpad name> (<launchpad locality>)``

we encourage you to use the date_unix for sorting it - and if 2 launches have the same date, use the first one in the API result.

Your code should not be executed when the file is imported (you should use ``if __name__ == '__main__':``)

## 4. How many by rocket?
By using the ``(unofficial) SpaceX API``, write a script that displays the number of launches per rocket.

- Use this [https://api.spacexdata.com/v3/launches](https://intranet.hbtn.io/rltoken/mE5gLKOkxll1QgYF4o2Rwg) to make ``request``
- All launches should be taking in consideration
- Each line should contain the rocket name and the number of launches separated by ``:`` (format below in the example)
- Order the result by the number launches (descending)
- If multiple rockets have the same amount of launches, order them by alphabetic order (A to Z)
- Your code should not be executed when the file is imported (you should use if __name__ == '__main__':)

# Versions
Python 3.9

requests 2.31.0
