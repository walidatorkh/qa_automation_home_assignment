import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.canadadealsonline.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def fill_search_box(setup, search_term):
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
def test_search_box_more_than_one_result(setup, search_term):
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
def test_search_box_appears_in_three_top_result(setup, search_term):
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


def test_search_box_no_appears_http_404_not_found_error(setup):
    driver = setup
    search_term = "Keyboard"
    try:
        search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_input.send_keys(search_term)
        # Update XPath expression to include the search term
        dropdown_results = driver.find_elements(By.XPATH,
                                                f"//span[contains(@class, 'text-blue-400') and contains(text(), 'keyboard')]")
        dropdown_results[0].click()
        # Check if the URL contains "404"
        assert "404" not in driver.current_url, f"Test case failed: 404 page found after clicking on search result for {search_term}"
    except NoSuchElementException:
        print("Element not found.")


@pytest.mark.parametrize("search_term", ["Keyboard", "Shower Carpet", "Air Fryer"])
def test_no_http_404(setup, search_term):
    driver = setup
    url = f"https://www.canadadealsonline.com/{search_term}"
    driver.get(url)
    assert "404" not in driver.page_source, f"HTTP 404: Page not found for URL: {url}"
