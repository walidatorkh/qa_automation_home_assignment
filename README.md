# qa_automation_home_assignment
## qa_automation_home_assignment

### This home assignment include couple of tasks:

1. Example of small test plan for search engine on site : https://www.canadadealsonline.com/

2. Tests (back end) of API calls for “Pokemon” ( https://pokeapi.co/)

3. Tests (front end) of the website "https://www.canadadealsonline.com/" and specific the search box

4. Added API testing for API https://petstore.swagger.io 
   to test API automation testing skills. 
   This is a basic API for managing a pet store app. 
   We use it just for documentation purposes, and the request you send will not be saved to the
   DB.
      1. Create new pet:
      - Design a POST request to create a new pet with "status": "available" in the pet
      store.
      - Update the pet to "status": "sold".
      * note that this api call will fail because this is a dummy api and not a real one.
      2. Find a pet by status:
      - Find a pet by status: “available”
      - Verify that the name of the fourth pet name is “Puff”.
      - Log the pet object to the console.
      3. Find another pet by status:
      - Find a pet by status: “sold”.
      - Validate that all the items that returned in the response have the expected status

# API Testing Checklist

## General Checklist

| Category                              | Description                                                                                  |
|---------------------------------------|----------------------------------------------------------------------------------------------|
| Proper Body                           | Verify that the request body is correctly formed as per the example.                         |
| Business Logic (Positive, Negative)   | Test both positive and negative scenarios for business logic.                                |
| Various Parameters                    | Test different parameters for their necessity and functionality.                             |
| Permutation of Elements               | Check permutation of elements in headers and body.                                           |
| Case Sensitivity                      | Verify case sensitivity in headers and body.                                                 |
| Malformed XML/JSON                    | Test with malformed XML/JSON and verify the error handling.                                  |

## Parameter Locations

| Location              | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| URL                   | Parameters passed in the URL.                                         |
| Headers               | Parameters passed in the headers.                                     |
| Body                  | Parameters passed in the body of the request.                         |
| Combination           | Combinations of the above locations.                                  |

## Parameter Testing

| Type                        | Description                                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------------------|
| Correct Parameter           | Verify with the correct parameter as per the example.                                            |
| Mandatory                   | Test what happens if the mandatory parameter is not provided.                                    |
| Business Logic              | Design tests based on business logic requirements.                                               |
| Case Sensitivity            | Verify case sensitivity if the parameter is text-based.                                          |
| Permutation of Parameters   | Check with different permutations of parameters.                                                 |

## Header Testing

| Type                      | Description                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------|
| Documentation Compliance  | Headers should work as per the documentation.                                                    |
| Mandatory Headers         | Test what happens if a mandatory header is not provided.                                         |
| Incorrect Headers         | Verify the error message when incorrect headers are provided.                                    |
| Positive Tests            | Headers should work as expected as per the documentation.                                        |
| Case Insensitivity        | Headers should be case insensitive.                                                              |

## Response Validation

| Type             | Description                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------|
| Status Code      | Validate the status code returned in the response.                                               |
| Body             | Check the body of the response for:                                                               |
|                  | - Fields returned                                                                                 |
|                  | - Values in the fields                                                                            |
|                  | - Error texts                                                                                     |

## Request Parameters

| Type                 | Description                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------|
| Mandatory            | Test what happens if a mandatory parameter is not provided.                                      |
| Permutation          | Check different permutations of parameters.                                                     |
| Business Logic       | Design tests based on business logic requirements.                                               |
| Case Sensitivity     | Verify case sensitivity if the parameter is text-based.                                          |

## Method Testing

| Type                       | Description                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Method Substitution        | Test by substituting the request method (e.g., POST to GET, POST to PUT).                       |
| Error Handling             | Ensure the error message is clear and understandable if method substitution fails.              |

## Response Body

| Type                     | Description                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------|
| Returned Fields          | Verify the fields returned in the response.                                                      |
| Field Values             | Check the values in the fields.                                                                  |
| Error Texts              | Verify the error texts returned in the response.                                                 |
| Compare with Documentation | Compare the fields and values with the documentation.                                          |
| Compare SOAP/REST        | If applicable, compare the response fields between SOAP and REST.                                |

## URL Parameters

| Type                 | Description                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------|
| Correct Parameter    | Verify with the correct parameter as per the example.                                            |
| Mandatory            | Test what happens if a mandatory parameter is not provided.                                      |
| Business Logic       | Design tests based on business logic requirements.                                               |
| Case Sensitivity     | Verify case sensitivity if the parameter is text-based.                                          |

## Empty Fields

| Type                     | Description                                                                                      |
|--------------------------|--------------------------------------------------------------------------------------------------|
| Absence of Data          | Test the response when a field is missing or empty in the request.                               |
| Empty Fields in Response | Verify how empty fields are handled in the response.                                             |
| SOAP vs REST             | Compare how SOAP and REST handle empty fields differently.                                       |

## Notes:
- **Response Time**: Record the time taken for each API call in milliseconds.
- **Pass/Fail**: Indicate whether the test passed or failed based on the expected and actual outcomes.


