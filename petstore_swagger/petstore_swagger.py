import requests
import logging

BASE_URL = "https://petstore.swagger.io/v2"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PetstoreAPI:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def create_new_pet(self, pet_id, name, category, tags):
        """
        Create a new pet with the status 'available'.
        """
        url = f"{self.base_url}/pet"
        headers = {'Content-Type': 'application/json'}
        data = {
            "id": pet_id,
            "name": name,
            "category": {"id": 1, "name": category},
            "photoUrls": [],
            "tags": [{"id": 1, "name": tag} for tag in tags],
            "status": "available"
        }

        response = requests.post(url, json=data, headers=headers)
        logger.info(f"Create Pet Response: {response.status_code} - {response.text}")
        return response.json()

    def update_pet_status(self, pet_id, status):
        """
        Update the status of an existing pet.
        """
        url = f"{self.base_url}/pet"
        headers = {'Content-Type': 'application/json'}
        data = {
            "id": pet_id,
            "status": status
        }

        response = requests.put(url, json=data, headers=headers)
        logger.info(f"Update Pet Status Response: {response.status_code} - {response.text}")
        return response.json()

    def find_pet_by_status(self, status):
        """
        Find pets by status.
        """
        url = f"{self.base_url}/pet/findByStatus?status={status}"
        response = requests.get(url)
        logger.info(f"Find Pet by Status Response: {response.status_code} - {response.text}")
        return response.json()

    def verify_fourth_pet_name(self, status, expected_name):
        """
        Verify that the name of the fourth pet with the given status is as expected.
        """
        pets = self.find_pet_by_status(status)
        if len(pets) >= 4:
            fourth_pet = pets[3]  # List is zero-indexed
            actual_name = fourth_pet.get('name')  # Get the pet's name from the response
            logger.info(f"Actual name of the fourth pet: {actual_name}")
            assert actual_name == expected_name, f"Expected name: {expected_name}, but got: {actual_name}"
            logger.info(f"Fourth pet name is correctly {expected_name}")
            logger.info(f"Fourth Pet Object: {fourth_pet}")
        else:
            logger.error("There are less than four pets available.")

    def validate_pets_status(self, status):
        """
        Validate that all pets returned by the status query have the expected status.
        """
        pets_with_status = []
        pets = self.find_pet_by_status(status)
        for pet in pets:
            assert pet['status'] == status, f"Pet ID {pet['id']} does not have the status {status}"
            pets_with_status.append(pet)
        logger.info(f"All pets with the status {status}: {pets_with_status}")
        return pets_with_status


# Example usage
if __name__ == "__main__":
    petstore_api = PetstoreAPI()

    # Create a new pet
    # new_pet = petstore_api.create_new_pet(pet_id=123456, name="Fido", category="Dogs", tags=["friendly", "playful"])

    # Update the pet status to 'sold'
    # petstore_api.update_pet_status(pet_id=123456, status="sold")

    # Find a pet by status 'available' and verify the fourth pet's name is 'Puff' will fail
    # petstore_api.verify_fourth_pet_name(status="available", expected_name="sample1") will work
    # petstore_api.verify_fourth_pet_name(status="available", expected_name="Puff")

    # Find a pet by status 'sold' and validate all returned pets have the status 'sold'
    # petstore_api.validate_pets_status(status="sold")
