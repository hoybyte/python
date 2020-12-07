from api import MovieSearchClient


def main():
    val = 'Nul'

    while val:
        print("What would you like to do next?")
        val = input('Search movies by: [k]eyword, [d]irector, [i]mdb code?')

        if val == 'k':
            read_post()
        elif val == 'd':
            MovieSearchClient.entries_by_director()
        elif val == 'i':
            MovieSearchClient.entry_by_imdbcode()


def read_post():
    keyword = input('What do you want to search by: ')
    svc = MovieSearchClient()
    response = svc.entries_by_search(keyword)

    posts = response.json()

    print(posts)


if __name__ == "__main__":
    main()
