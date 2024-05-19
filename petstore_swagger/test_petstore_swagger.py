import pytest
from petstore_swagger import PetstoreAPI  # Ensure this matches the actual filename and class name

"""
     Examples of possible tests scenarios...
"""


BASE_URL = "https://petstore.swagger.io/v2"


@pytest.fixture
def petstore_api():
    return PetstoreAPI(BASE_URL)


def test_create_new_pet(petstore_api):
    new_pet = petstore_api.create_new_pet(pet_id=123456, name="Fido", category="Dogs", tags=["friendly", "playful"])
    assert new_pet['name'] == "Fido"
    assert new_pet['status'] == "available"


def test_update_pet_status(petstore_api):
    updated_pet = petstore_api.update_pet_status(pet_id=123456, status="sold")
    assert updated_pet['status'] == "sold"


def test_find_pet_by_status_available(petstore_api):
    pets = petstore_api.find_pet_by_status("available")
    if len(pets) >= 4:
        assert pets[3]['name'] == "Puff"
    else:
        pytest.skip("Less than four pets available, skipping the test.")


def test_find_pet_by_status_sold(petstore_api):
    pets = petstore_api.find_pet_by_status("sold")
    for pet in pets:
        assert pet['status'] == "sold"


def test_print_elements_text(capsys, petstore_api):
    pets = petstore_api.find_pet_by_status("sold")
    for pet in pets:
        print(pet)
    captured = capsys.readouterr()
    for pet in pets:
        assert str(pet) in captured.out


if __name__ == "__main__":
    pytest.main()
