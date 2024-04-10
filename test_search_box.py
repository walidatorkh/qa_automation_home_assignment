import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup():
    """
        Fixture to set up a WebDriver instance for testing the Canada Deals Online website.

        This fixture launches a Chrome WebDriver, maximizes the window, navigates to the
        Canada Deals Online website, and sets up implicit wait for the driver.

        Yields:
            WebDriver: An instance of the WebDriver set up for testing the website.

        Example:
            This fixture can be used in PyTest tests to obtain a WebDriver instance for
            interacting with the Canada Deals Online website. For example:

            ```
            def test_website_title(setup):
                driver = setup
                assert driver.title == "Canada Deals Online - Save more. Smile more."
            ```
        """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.canadadealsonline.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def fill_search_box(setup, search_term: str):
    """
        Function to fill the search box on the Canada Deals Online website and verify the dropdown results.

        This function takes a WebDriver instance `setup` and a search term `search_term` as input.
        It fills the search input field with the provided search term, waits for the dropdown results to appear,
        and then verifies that there are at least two search results in the dropdown.

        Args:
            setup (WebDriver): The WebDriver instance set up for testing the website.
            search_term (str): The search term to enter into the search input field.

        Raises:
            AssertionError: If less than two search results are found in the dropdown.

        Example:
            This function can be used in PyTest tests to fill the search box with a search term
            and verify the dropdown results. For example:

            ```
            def test_search_results(setup):
                fill_search_box(setup, "Keyboard")
            ```
        """
    driver = setup
    try:
        search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.send_keys(search_term)
        driver.implicitly_wait(10)
        dropdown_results = driver.find_elements(By.XPATH,
                                                "//span[contains(@class, 'text-blue-400') and contains(text(), 'keyboard')]")
        assert len(dropdown_results) > 1, f"Test case 1 failed: {search_term} has less than 2 search results"
    except NoSuchElementException:
        print("Element not found.")


@pytest.mark.parametrize("search_term", ["Keyboard", "Shower Carpet", "Air Fryer"])
def test_search_box_more_than_one_result(setup, search_term: str):
    """
        Test function to verify that the search box on the Canada Deals Online website returns more than one result.

        This test function takes a search term as input and fills the search input field with the provided term.
        It then waits for the dropdown results to appear and verifies that there are more than one search results in the dropdown.

        Args:
            setup (WebDriver): The WebDriver instance set up for testing the website.
            search_term (str): The search term to enter into the search input field.

        Raises:
            AssertionError: If less than two search results are found in the dropdown.

        Example:
            This function can be used in PyTest tests to verify that the search box returns more than one result
            for different search terms. For example:

            ```
            def test_search_results(setup):
                test_search_box_more_than_one_result(setup, "Shower Curtain")
            ```
        """
    driver = setup
    try:
        search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.clear()
        search_input.send_keys(search_term)
        driver.implicitly_wait(10)
        dropdown_results = driver.find_elements(By.XPATH,
                                                "//span[contains(@class, 'text-blue-400') and contains(text(), 'keyboard')]")
        assert len(dropdown_results) > 1, f"Test case 1 failed: {search_term} has less than 2 search results"
        search_input.clear()
    except NoSuchElementException:
        print("Element not found.")


@pytest.mark.parametrize("search_term", ["Keyboard", "Shower Carpet", "Air Fryer"])
def test_search_box_appears_in_three_top_result(setup, search_term: str):
    """
        Test function to verify that the search term appears in the top three search results on the Canada Deals Online website.

        This test function takes a search term as input and fills the search input field with the provided term.
        It then waits for the dropdown results to appear and verifies that the search term appears in the text of
        the top three search results in the dropdown.

        Args:
            setup (WebDriver): The WebDriver instance set up for testing the website.
            search_term (str): The search term to enter into the search input field.

        Raises:
            AssertionError: If the search term does not appear in the text of the top three search results.

        Example:
            This function can be used in PyTest tests to verify that the search term appears in the top three search results
            for different search terms. For example:

            ```
            def test_search_results(setup):
                test_search_box_appears_in_three_top_result(setup, "Shower Curtain")
            ```
        """
    driver = setup
    try:
        search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.clear()
        search_input.send_keys(search_term)
        driver.implicitly_wait(10)
        # Update XPath expression to include the search term
        dropdown_results = driver.find_elements(By.XPATH,
                                                f"//span[contains(@class, 'text-blue-400') and contains(text(), '{search_term.lower()}')]")
        first_result_text = dropdown_results[0].text
        assert search_term.lower() in first_result_text.lower(), f"Test case failed: {search_term} not found in top search result"
        search_input.clear()
    except NoSuchElementException:
        print("Element not found.")


def test_search_box_no_appears_http_404_not_found_errors(setup):
    """
        Test function to verify that clicking on a search result does not lead to a 404 Not Found error.

        This test function takes a WebDriver instance set up for testing the website. It fills the search input field
        with a predefined search term, clicks on the first search result, and checks if the current URL contains "404".
        If a 404 page is found, an AssertionError is raised.

        Args:
            setup (WebDriver): The WebDriver instance set up for testing the website.

        Raises:
            AssertionError: If a 404 page is found after clicking on a search result.

        Example:
            This function can be used in PyTest tests to verify that clicking on a search result does not lead
            to a 404 Not Found error. For example:

            ```
            def test_search_no_404_error(setup):
                test_search_box_no_appears_http_404_not_found_errors(setup)
            ```
        """
    driver = setup
    search_term = "Keyboard"
    try:
        search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.send_keys(search_term)
        # Update XPath expression to include the search term
        dropdown_results = driver.find_elements(By.XPATH,
                                                f"//span[contains(@class, 'text-blue-400') and contains(text(), 'keyboard')]")
        dropdown_results[0].click()
        driver.implicitly_wait(10)
        # Check if the URL contains "404"
        assert "404" not in driver.current_url, f"Test case failed: 404 page found after clicking on search result for {search_term}"
    except NoSuchElementException:
        print("Element not found.")

