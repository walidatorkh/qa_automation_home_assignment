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
