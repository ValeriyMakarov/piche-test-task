from datetime import datetime as dtime
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import logging

log = logging.getLogger(__name__)


def get_formatted_time() -> str:
    return dtime.now().strftime("%b-%d-%Y.%H.%M.%S")


def make_screenshot(driver: WebDriver) -> None:
    driver.save_screenshot(f"test_run_data/UI.{get_formatted_time()}.png")

'''Creates screenshot of site and logs info while waiting for page to load.'''
def wait_for_page_to_load(driver: WebDriver, wait_time: int = 5) -> None:
    log.info(f"Waiting {wait_time} seconds for page to load.")
    WebDriverWait(driver, wait_time).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    log.info(f"Page is loaded.")
    make_screenshot(driver)
