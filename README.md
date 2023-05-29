# Lord of the Rings SDK

The Lord of the Rings SDK provides a Python interface for interacting with the Lord of the Rings API.

## Features:
- Get movies by ID or retrieve all movies
- Get quotes by ID or retrieve all quotes for a movie

## Installation

To install the Lord of the Rings SDK, follow these steps:

- Clone the repository:
git clone https://github.com/ovatalar/ovatalar-lotr-sdk.git

- Change to the project directory:
cd ovatalar-lotr-sdk

- Install the dependencies:
pip install -r requirements.txt

- Done

## Usage

- Import the LotrClient class:
from lotr_sdk.lotr_client import LotrClient

- Create an instance of LotrClient with the base URL of the Lord of the Rings API:
client = LotrClient("https://api.ova-lotr-sdk.com")

- Use the available methods to interact with the API
# Get a movie by ID
movie = client.get_movie(1)

# Get quotes from a movie
quotes = client.get_movie_quote(1)

# Get a quote by ID
quote = client.get_quote(1)

## Testing

python -m unittest discover tests
