from datetime import datetime as dtime
import logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pytest import fixture
from os import mkdir, path

TEST_RUN_DATA_DIR_PATH = "test_run_data"

'''Creates headless connection with the site.'''
@fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    browser.get("http://example.com/")
    yield browser
    browser.quit()


'''Creates directory for logs and configures logger.'''
def pytest_configure(config):
    if not path.exists(TEST_RUN_DATA_DIR_PATH):
        mkdir(TEST_RUN_DATA_DIR_PATH)
    timestamp = dtime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = path.join(TEST_RUN_DATA_DIR_PATH, f'{timestamp}.log')
    logging.basicConfig(
        filename=log_file,
        format="[%(levelname)s] %(asctime)s : %(funcName)s : - %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
