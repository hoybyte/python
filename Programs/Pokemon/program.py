from api import find_pokemon_from_name
import random


def main():
    # Insert Pokemon Number in Function
    poke = random.randrange(1, 151, 1)
    # poke = input("What pokemon do you want? ")
    find_pokemon_from_name(poke)


if __name__ == "__main__":
    main()
