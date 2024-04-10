import requests


def check_api_call_with_data(type_id_or_name, api_type="pokemon-species"):
    url = f"https://pokeapi.co/api/v2/{api_type}/{type_id_or_name}/"

    # Make the API call
    response = requests.get(url)

    # Check if the response is successful (status code 200) and if it contains data
    if response.status_code == 200:
        data = response.json()
        if data:
            print("Success - API call has data")
            return True
        else:
            print("Error - API call successful but no data found")
            return False
    else:
        print(f"Error - API call failed with status code {response.status_code}")
        return False


def check_api_call_no_data(type_id_or_name, api_type="pokemon-species"):
    url = f"https://pokeapi.co/api/v2/{api_type}/{type_id_or_name}/"

    # Make the API call
    response = requests.get(url)

    # Check if the response is successful (status code 200) and if it contains no data
    if response.status_code == 200:
        data = response.json()
        if not data:
            print("Success - API call successful and no data found")
            return True
        else:
            print("Error - API call has data")
            return False
    else:
        print(f"Error - API call failed with status code {response.status_code}")
        return False


def check_api_call_server_error():
    url = f"https://pokeapi.co/api/v2/type/"
    response = requests.get(url)
    # Check if the response is a server error (status code 5xx)
    if 500 <= response.status_code < 600:
        return True
    else:
        print(response)
        return False


def compare_pokemon_names(id):
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
