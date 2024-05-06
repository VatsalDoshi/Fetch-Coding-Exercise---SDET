import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from config import URL

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    try:
        from selenium import webdriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get(URL)
        return driver
    except Exception as e:
        logging.error(f"Failed to setup the driver: {e}")
        raise

def click_button(driver, button_id):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, button_id))
        )
        button.click()
        logging.info(f"Clicked button {button_id}")
    except TimeoutException:
        logging.error("Button click timed out.")
    except NoSuchElementException:
        logging.error("Button not found.")
    except Exception as e:
        logging.error(f"An error occurred while clicking the button: {e}")

def enter_bar_numbers(driver, left_bars, right_bars):
    try:
        for i, bar in enumerate(left_bars):
            input_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f'#left-{i}'))
            )
            input_field.send_keys(str(bar))
        
        for i, bar in enumerate(right_bars):
            input_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, f'#right-{i}'))
            )
            input_field.send_keys(str(bar))
    except TimeoutException:
        logging.error("Timeout while entering bar numbers.")
    except Exception as e:
        logging.error(f"An error occurred while entering bar numbers: {e}")

def get_weighing_result(driver):
    try:
        result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#result'))
        )
        return result.text
    except TimeoutException:
        logging.error("Timeout while getting the weighing result.")
    except Exception as e:
        logging.error(f"An error occurred while getting the weighing result: {e}")

def reset_scale(driver):
    try:
        reset_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#reset'))
        )
        reset_button.click()
        logging.info("Scale reset successfully.")
    except TimeoutException:
        logging.error("Timeout while trying to reset the scale.")
    except Exception as e:
        logging.error(f"An error occurred while resetting the scale: {e}")
