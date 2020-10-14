# To run this test on your own PC you will need to have downloaded and configured the correct chromedriver for your
# operating system and version of the Chrome browser. See https://chromedriver.chromium.org
# You are not expected to be able to do this for COMP0035, this is for illustration purposes so you can start to
# see what is possible.

import time

import pytest
import urllib3
from selenium import webdriver
from flask import url_for
from selenium.webdriver.support.select import Select

from app import create_app


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.debug = True
    return app


# Fixture for Chromedriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.usefixtures('live_server')
def test_access_to_live_server(live_server):
    http = urllib3.PoolManager()
    result = http.request('GET', url_for('index', _external=True))
    assert result.status == 200


def test_h1_contains_calculator(client, driver, selenium):
    # Navigate to the homepage
    driver.get(url_for('index', _external=True))
    # Wait for 5 seconds
    driver.implicitly_wait(5)
    # Get the text contents of first heading which has an id of 'heading_1'
    h1 = driver.find_element_by_id('heading_1').text
    # Check that the text includes the word 'Calculator'
    assert 'Calculator' in str(h1)


def test_add_returns_result_page(client, driver, selenium):
    # Navigate to the homepage
    driver.get(url_for('index', _external=True))
    driver.implicitly_wait(10)

    # Locate the inputs in the form and enter the values
    driver.find_element_by_id("first_term").send_keys(5)
    driver.find_element_by_id("second_term").send_keys(7)
    operation = Select(driver.find_element_by_id("operation"))
    operation.select_by_visible_text('Add')
    driver.find_element_by_id("submit").click()
    driver.implicitly_wait(10)
    # Assert that browser redirects to the result page
    assert (url_for('result') in str(driver.current_url))


def test_add_returns_correct_result(driver, live_server, client):
    # Navigate to the homepage
    driver.get(url_for('index', _external=True))
    time.sleep(3)

    # Locate the inputs in the form and enter the values 5 and 7
    driver.find_element_by_id("first_term").send_keys(5)
    driver.find_element_by_id("second_term").send_keys(7)
    operation = Select(driver.find_element_by_id("operation"))
    operation.select_by_visible_text('Add')
    time.sleep(3)
    driver.find_element_by_id("submit").click()

    # Assert that the text in the html tag with an id of 'result' is 12
    result = driver.find_element_by_id("result").text
    assert '12' in str(result)
