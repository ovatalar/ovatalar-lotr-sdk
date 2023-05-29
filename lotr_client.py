# file: lotr_client.py

import requests

class LotrClient:
    """
    Class: LotrClient
    Description: Represents a client for interacting with the Lord of the Rings API.
    """

    def __init__(self, base_url):
        """
        Method: __init__
        Description: Initializes an instance of the LotrClient class with the base URL of the API.
        Parameters:
            - base_url (str): The base URL of the Lord of the Rings API.
        """
        self.base_url = base_url

    def get_movie(self, movie_id):
        """
        Method: get_movie
        Description: Retrieves a movie by ID from the Lord of the Rings API.
        Parameters:
            - movie_id (int): The ID of the movie.
        Returns:
            - dict: The movie data.
        """
        url = f"{self.base_url}/movie/{movie_id}"
        response = requests.get(url)
        return response.json()

    def get_movie_quote(self, movie_id):
        """
        Method: get_movie_quote
        Description: Retrieves quotes for a movie from the Lord of the Rings API.
        Parameters:
            - movie_id (int): The ID of the movie.
        Returns:
            - list: The quotes associated with the movie.
        """
        url = f"{self.base_url}/movie/{movie_id}/quote"
        response = requests.get(url)
        return response.json()

    def get_quote(self, quote_id):
        """
        Method: get_quote
        Description: Retrieves a quote by ID from the Lord of the Rings API.
        Parameters:
            - quote_id (int): The ID of the quote.
        Returns:
            - dict: The quote data.
        """
        url = f"{self.base_url}/quote/{quote_id}"
        response = requests.get(url)
        return response.json()
