import requests
import uplink

from uplink_helpers import raise_for_status


@raise_for_status
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(baseurl='https://movieservice.talkpython.fm/')

    @uplink.get('/api/search/{keyword}')
    def entries_by_search(self, keyword) -> requests.models.Response:
        """ Retrieves movies by search keyword. """

    @uplink.get('api/director/{director_name}')
    def entries_by_director(self, director_name) -> requests.models.Response:
        """ Retrieves movie titles by Director name. """

    @uplink.get('api/movie/{imdb_number}')
    def entry_by_imdbcode(self, imdb_number) -> requests.models.Response:
        """ Retrives Movie by imdb code. """
