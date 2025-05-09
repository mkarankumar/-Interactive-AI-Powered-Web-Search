from link_collection import googlesearch
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import urllib.parse 

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_dynamic_website(url):
    # Initialize the Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except Exception as e:
        logging.error(f"Error initializing Chrome driver: {e}")
        print(f"Error initializing Chrome driver: {e}")
        return
    try:
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url  
        parsed_url = urllib.parse.urlparse(url)
        if not parsed_url.netloc:
            raise ValueError(f"Invalid URL: {url}") 

        driver.get(url)
        logging.info(f"Navigated to: {url}")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        logging.info("Page loaded.")
        page_text = driver.find_element(By.TAG_NAME, 'body').text
        logging.info("Text extracted.")
        print(page_text)

    except ValueError as ve:
        logging.error(f"Invalid URL provided: {ve}")
        print(f"Invalid URL provided: {ve}")
    except Exception as e:
        logging.error(f"Error during scraping: {e}")
        print(f"Error during scraping: {e}")
    finally:
        driver.quit()
        logging.info("Driver quit.")


