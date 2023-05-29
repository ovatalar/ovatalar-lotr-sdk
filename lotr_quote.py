# file: lotr_quote.py

class LotrQuote:
    """
    Class: LotrQuote
    Description: Represents a quote from the Lord of the Rings universe.
    """

    def __init__(self, quote_data):
        """
        Method: __init__
        Description: Initializes an instance of the LotrQuote class with the quote data.
        Parameters:
            - quote_data (dict): The data of the quote.
        """
        self.quote_data = quote_data

    def get_id(self):
        """
        Method: get_id
        Description: Get the ID of the quote.
        Returns:
            - int: The ID of the quote.
        """
        return self.quote_data.get("id")

    def get_content(self):
        """
        Method: get_content
        Description: Get the content of the quote.
        Returns:
            - str: The content of the quote.
        """
        return self.quote_data.get("content")
