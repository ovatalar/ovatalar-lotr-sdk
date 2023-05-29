# File: test_lotr_sdk.py

import unittest
from lotr_client import LotrClient
from lotr_movie import LotrMovie
from lotr_quote import LotrQuote


class LotrSdkTestCase(unittest.TestCase):

    def setUp(self):
        self.client = LotrClient("https://api.ova-lotr-sdk.com")

    def test_get_movie(self):
        movie = self.client.get_movie(1)
        self.assertIsInstance(movie, dict)
        self.assertEqual(movie["id"], 1)

    def test_get_movie_quote(self):
        quotes = self.client.get_movie_quote(1)
        self.assertIsInstance(quotes, list)
        if quotes:
            quote = quotes[0]
            self.assertIsInstance(quote, dict)
            self.assertIn("id", quote)

    def test_get_quote(self):
        quote = self.client.get_quote(1)
        self.assertIsInstance(quote, dict)
        self.assertEqual(quote["id"], 1)

    def test_lotr_movie(self):
        movie_data = {"id": 1, "title": "The Fellowship of the Ring", "year": 2001}
        movie = LotrMovie(movie_data)
        self.assertEqual(movie.get_id(), 1)
        self.assertEqual(movie.get_title(), "The Fellowship of the Ring")
        self.assertEqual(movie.get_year(), 2001)

    def test_lotr_quote(self):
        quote_data = {"id": 1, "character": "Gandalf", "quote": "You shall not pass!"}
        quote = LotrQuote(quote_data)
        self.assertEqual(quote.get_id(), 1)
        self.assertEqual(quote.get_character(), "Gandalf")
        self.assertEqual(quote.get_quote(), "You shall not pass!")


if __name__ == "__main__":
    unittest.main()
