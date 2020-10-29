from typing import List

import requests
import collections

Pokemon = collections.namedtuple('Pokemon', 'name, weight')


def find_pokemon_from_name(id: str) -> List[Pokemon]:
    url = f'https://pokeapi.co/api/v2/pokemon/{id}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    print(results['name'])
