import pytest 
from playwright.sync_api import sync_playwright
import re 
import requests


@pytest.fixture(scope='function')
def playwright():
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        context = browser.new_page()
        yield context 
        browser.close()


@pytest.fixture(scope='function')
def page(playwright):
    return playwright











