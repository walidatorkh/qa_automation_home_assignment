import random
from unittest.mock import patch, Mock

import check_pokeapi
import pytest
from unittest.mock import patch

from requests.exceptions import RequestException


def generate_random_id():
    return random.randint(1, 50)


@pytest.mark.parametrize("type_id_or_name, api_type, expected_result", [
    ("25", "pokemon-species", True),  # Pikachu - data should be available
    ("27", "pokemon", True),
    ("pikachu", "pokemon", True),  # Pikachu - data should be available
    ("5000", "pokemon-species", False)  # Non-existent Pokémon ID - no data
])
def test_check_api_call_with_data(type_id_or_name, api_type, expected_result):
    assert check_pokeapi.check_api_call_with_data(type_id_or_name, api_type=api_type) == expected_result


@pytest.mark.parametrize("type_id_or_name, api_type, expected_result", [
    ("25", "pokemon-species", False),  # Pikachu - data should be available
    ("pikachu", "pokemon", False),  # Pikachu - data should be available
    ("5000", "pokemon-species", False)  # Non-existent Pokémon ID - no data
])
def test_check_api_call_no_data(type_id_or_name, api_type, expected_result):
    assert check_pokeapi.check_api_call_no_data(type_id_or_name, api_type=api_type) == expected_result


# @pytest.mark.parametrize("type_id_or_name, api_type", [
#     ("25", "pokemon-species"),  # Pikachu - data should be available
#     ("pikachu", "pokemon"),  # Pikachu - data should be available
#     ("5000", "pokemon-species")  # Non-existent Pokémon ID - no data
# ])
def test_check_api_call_server_error():
    with patch('requests.get') as mock_get:
        # Simulating a server error response
        mocked_response = Mock()
        mocked_response.status_code = 503
        mock_get.return_value = mocked_response

        # Call the function under test
        result = check_pokeapi.check_api_call_server_error()

        # Assertions
        assert result is True  # Expecting a server error


@pytest.mark.parametrize("pokemon_id, expected_result", [
    (generate_random_id(), True),
    (generate_random_id(), True),
    (generate_random_id(), True),
    (5000, None)  # Non-existent Pokémon ID - None should be returned
])
def test_compare_pokemon_names(pokemon_id, expected_result):
    assert check_pokeapi.compare_pokemon_names(pokemon_id) == expected_result

# Run the test using: pytest -s test_api.py
