# file: lotr_movie.py

class LotrMovie:
    """
    Class: LotrMovie
    Description: Represents a movie from the Lord of the Rings universe.
    """

    def __init__(self, movie_data):
        """
        Method: __init__
        Description: Initializes an instance of the LotrMovie class with the movie data.
        Parameters:
            - movie_data (dict): The data of the movie.
        """
        self.movie_data = movie_data

    def get_id(self):
        """
        Method: get_id
        Description: Get the ID of the movie.
        Returns:
            - int: The ID of the movie.
        """
        return self.movie_data.get("id")

    def get_title(self):
        """
        Method: get_title
        Description: Get the title of the movie.
        Returns:
            - str: The title of the movie.
        """
        return self.movie_data.get("title")

    def get_quotes(self):
        """
        Method: get_quotes
        Description: Get the quotes associated with the movie.
        Returns:
            - list: The quotes associated with the movie.
        """
        return self.movie_data.get("quotes", [])
