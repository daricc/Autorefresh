import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import WebDriverException
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

# URL to refresh
url = 'https://example.com'  # Replace with the URL you want to refresh

def refresh_url_with_edge(url):
    """
    Continuously refreshes the given URL using Microsoft Edge in headless mode.
    This function sets up the Edge WebDriver with headless options, starts the WebDriver service,
    and refreshes the specified URL at a 30-second interval. If a WebDriverException occurs, it logs
    the error and quits the driver.
    Args:
        url (str): The URL to be refreshed.
    Raises:
        WebDriverException: If an error occurs while interacting with the WebDriver.
    """
    try:
        # Set up Edge options
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")  # Run headless if you don't need a UI

        # Start the WebDriver service
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)

        # Refresh the URL at an interval
        while True:
            driver.get(url)
            logging.info(f"Refreshed URL: {url}")
            time.sleep(30)  # Refresh every 30 seconds

    except WebDriverException as e:
        logging.error(f"WebDriverException occurred: {e}")

    finally:
        driver.quit()

def refresh_url_with_chrome(url):
    try:
        # Set up Chrome options
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")  # Run headless if you don't need a UI

        # Start the WebDriver service
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Refresh the URL at an interval
        while True:
            driver.get(url)
            logging.info(f"Refreshed URL: {url}")
            time.sleep(30)  # Refresh every 30 seconds

    except WebDriverException as e:
        logging.error(f"WebDriverException occurred: {e}")

    finally:
        driver.quit()

# Uncomment the function you want to use
# refresh_url_with_edge(url)
# refresh_url_with_chrome(url)