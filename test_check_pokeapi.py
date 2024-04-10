import requests
import json
import random
import pytest


def compare_pokemon_names(id: str):
    """
        Compares the Pokemon names obtained from two different endpoints of the PokeAPI.
        :param id: The ID of the Pokemon to compare.
        :return: True if the names obtained from both endpoints match, False otherwise.
    """
    # Make API call to retrieve Pokemon name from the first endpoint
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    response_pokemon = requests.get(pokemon_url)
    if response_pokemon.status_code != 200:
        print(f"Error - Unable to retrieve data from {pokemon_url}")
        return None
    pokemon_data = response_pokemon.json()
    pokemon_name_pokemon_endpoint = pokemon_data['name']

    # Make API call to retrieve Pokemon name from the second endpoint
    species_url = f"https://pokeapi.co/api/v2/pokemon-species/{id}/"
    response_species = requests.get(species_url)
    if response_species.status_code != 200:
        print(f"Error - Unable to retrieve data from {species_url}")
        return None
    species_data = response_species.json()
    pokemon_name_species_endpoint = species_data['name']

    # Compare the names obtained from both endpoints
    if pokemon_name_pokemon_endpoint == pokemon_name_species_endpoint:
        print(f"The Pokémon name from both endpoints is: {pokemon_name_pokemon_endpoint}")
        return True
    else:
        print("Error - The Pokémon names obtained from both endpoints do not match.")
        print(f"Name from Pokemon endpoint: {pokemon_name_pokemon_endpoint}")
        print(f"Name from Species endpoint: {pokemon_name_species_endpoint}")
        return False


def generate_random_id():
    """
        Generates a random Pokémon ID between 1 and 50.

        This function generates a random integer representing a Pokémon ID.
        The generated ID falls within the range of IDs available in the Pokémon database,
        which is between 1 and 50.

        :return: Randomly generated Pokémon ID.
    """
    return random.randint(1, 50)


def pokeapi_get(type_id_or_name: str, api_type: str = "pokemon-species") -> json:
    """
    This function perform API calls
    :param type_id_or_name:
    :param api_type:
    :return:
    """
    url = f"https://pokeapi.co/api/v2/{api_type}/{type_id_or_name}/"
    # Make the API call
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


@pytest.mark.parametrize("type_id_or_name, api_type, name", [
    ("25", "pokemon-species", 'pikachu'),  # Pikachu - data should be available
    ("27", "pokemon", 'sandshrew'),  # Pikachu - data should be available
    ("12", "pokemon", 'butterfree'),  # Pikachu - data should be available
])
def test_smoke(
        type_id_or_name: str,
        api_type: str,
        name: str):
    """
    Test function to perform a smoke test on PokeAPI.
    :param type_id_or_name: The ID or name of the type to be queried.
    :param api_type: The type of API endpoint to be tested ('pokemon-species' or 'pokemon').
    :param name: The expected name to compare the result against (optional).
    """
    body = pokeapi_get(type_id_or_name, api_type)
    if name:
        assert body, "returned JSON is empty"
        assert name == body['name'], f'wrong result: expected {name} got {body["name"]}'
    else:
        assert not body, 'Got response body - not as expected'


@pytest.mark.parametrize("type_id_or_name, api_type", [
    ("pikachu111", "pokemon"),  # data should be not available
    ("50000", "pokemon-species"),  # data should be not available
])
def test_smoke_bad_path(
        type_id_or_name: str,
        api_type: str):
    """
    Checks that a request to unavailable data in PokeAPI raises an HTTPError.
    :param type_id_or_name: ID or name of the object that does not exist in the API.
    :param api_type: Type of object for the request (e.g., "pokemon").
    """
    with pytest.raises(requests.HTTPError) as excinfo:
        body = pokeapi_get(type_id_or_name, api_type)
    assert excinfo.value.response.status_code >= 300
    assert "Not Found" in str(excinfo.value)


@pytest.mark.parametrize("pokemon_id", ["27"])
def test_compare_id(pokemon_id: str):
    """
    Test function to compare Pokémon names retrieved from different endpoints of the PokeAPI.

    This test function retrieves the Pokémon names for a given Pokémon ID from two different
    endpoints of the PokeAPI and compares them. If the names are not the same, an assertion error is raised.

    :param pokemon_id: The ID of the Pokémon to retrieve from the API.
    """
    # Retrieve Pokémon names from different endpoints of the PokeAPI
    body_pokemon_types = pokeapi_get(pokemon_id, "pokemon-species")
    body_pokemon = pokeapi_get(pokemon_id, "pokemon")

    # Extract Pokémon names from the responses
    pokemon_name_from_types = body_pokemon_types["name"]
    pokemon_name_from_pokemon = body_pokemon["name"]

    # Compare retrieved Pokémon names
    assert pokemon_name_from_types == pokemon_name_from_pokemon, \
        f"Names retrieved from endpoint ({pokemon_name_from_types}) " \
        f"and 'pokemon' endpoint ({pokemon_name_from_pokemon}) are not the same"


@pytest.mark.parametrize("pokemon_id, expected_result", [
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (5000, None)  # Non-existent Pokémon ID - None should be returned
])
def test_compare_pokemon_names(pokemon_id: str, expected_result: str):
    """
        Tests the functionality of comparing Pokémon names using the PokeAPI.

        This test function checks if the comparison of Pokémon names returned from the PokeAPI
        matches the expected result.

        :param pokemon_id: ID of the Pokémon to compare.
        :param expected_result: Expected result of the comparison. If the Pokémon exists,
                                the expected result is a boolean indicating whether the names match.
                                If the Pokémon does not exist, the expected result is None.
    """
    assert compare_pokemon_names(pokemon_id) == expected_result

