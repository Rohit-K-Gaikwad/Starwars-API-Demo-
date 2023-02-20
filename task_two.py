"""
The task 2 goes like following:
Pull data for the first movie in star wars
Write the json data into a file named output.txt


SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

import json
import requests
import argparse

from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url, fetch_data

FIRST_FILM_URL = "https://swapi.dev/api/films/1/"


def first_film_data() -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""

    response = requests.get(FIRST_FILM_URL)

    result_ = response.json()

    write_data_into_file(result_)
    return result_


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("output.txt", "w") as fp:

        fp.write(json.dumps(data))


def characters_data(data_: Dict, resource: str) -> List:
    """pull data from swapi characters name sequentially for first film"""

    characters = data_.get(resource)  # returns None by default
    char_names = []

    for character in characters:
        character_data = hit_url(character)

        character_data = character_data.json()
        char_names.append(character_data.get("name"))

    # all_characters = fetch_data(characters)
    # for character in all_characters:
    #     char_names.append(character.get("name"))

    return char_names


def planets_data(data_: Dict, resource: str) -> List:
    """pull data from swapi planets name sequentially for first film"""

    planets = data_.get(resource)  # returns None by default

    planets_names = []
    for planet in planets:
        planets_data = hit_url(planet)

        planet_data = planets_data.json()
        planets_names.append(planet_data.get("name"))

    return planets_names


def vehicles_data(data_: Dict, resource: str) -> List:
    """pull data from swapi vehicles name sequentially for first film"""

    vehicles = data_.get("{}".format(resource))  # returns None by default

    vehicles_names = []
    for vehicle in vehicles:
        vehicles_data = hit_url(vehicle)

        vehicle_data = vehicles_data.json()
        vehicles_names.append(vehicle_data.get("name"))

    return vehicles_names


def species_data(data_: Dict, resource: str) -> List:
    """pull data from swapi species name sequentially for first film"""

    species = data_.get("{}".format(resource))  # returns None by default

    species_names = []
    for specie in species:
        species_data = hit_url(specie)

        species_data = species_data.json()
        species_names.append(species_data.get("name"))

    return species_names


def starships_data(data_: Dict, resource: str) -> List:
    """pull data from swapi species name sequentially for first film"""

    starships = data_.get("{}".format(resource))  # returns None by default

    starships_names = []
    for starship in starships:
        starships_data = hit_url(starship)

        starships_data = starships_data.json()
        starships_names.append(starships_data.get("name"))

    return starships_names


def main():
    """parse data to methods and fetch data according to user inputs. default = `characters` """

    parser = argparse.ArgumentParser(
        prog="starwarsAPI",
        usage="Fetches resources from swapi.dev for films based "
              "on whatever arguments we provide",
        description="It uses planet, characters, vehicles and uses requests library "
                    "to get values from the swapi.dev for first film"
    )

    # we are creating an option to get respective data
    parser.add_argument('-c', '--char', type=str,
                        default="characters",
                        help="helps to fetch data of characters from first film")
    parser.add_argument('-p', '--planet', type=str,
                        help="helps to fetch data of planets from first film")
    parser.add_argument('-v', '--vehicle', type=str,
                        help="helps to fetch data of vehicles from first film")
    parser.add_argument('-s', '--specie', type=str,
                        help="helps to fetch data of species from first film")
    parser.add_argument('-S', '--starship', type=str,
                        help="helps to fetch data of starships from first film")

    arguments = parser.parse_args()

    print(f"parsed arguments are - {arguments}")

    # first task
    first_result = first_film_data()
    print(f"First Film Data: \n")
    pprint(first_result)

    if arguments.char == "characters":
        char_result = characters_data(first_result, arguments.char)
        print(f"\nCharacters in First film: ", end="")
        pprint(char_result)

    if arguments.planet == "planets":
        planet_result = planets_data(first_result, arguments.planet)
        print(f"\nPlanets in First Film: ", end="")
        pprint(planet_result)

    if arguments.vehicle == "vehicles":
        vehicle_result = vehicles_data(first_result, arguments.vehicle)
        print(f"\nVehicles in First Film:", end="")
        pprint(vehicle_result)

    if arguments.specie == "species":
        species_result = species_data(first_result, arguments.specie)
        print(f"\nSpecies in First Film: ", end="")
        pprint(species_result)

    if arguments.starship == "starships":
        starships_result = starships_data(first_result, arguments.starship)
        print(f"\nStarships in First Film: ", end="")
        pprint(starships_result)


if __name__ == "__main__":

    main()
