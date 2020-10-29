from api import find_pokemon_from_name


def main():
    # Insert Pokemon Number in Function
    poke = input("What pokemon do you want? ")
    find_pokemon_from_name(poke)
    print(find_pokemon_from_name(poke))
    pass


if __name__ == "__main__":
    main()
