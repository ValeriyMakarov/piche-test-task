from selenium import webdriver
from pytest import fixture

@fixture()
def driver():
    browser = webdriver.Firefox()
    browser.get('http://example.com/')
    yield browser
    browser.quit()