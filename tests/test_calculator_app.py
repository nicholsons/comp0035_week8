import pytest

from calculator_app.app import create_app


@pytest.fixture(scope='session')
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_index_page_valid(client):
    """
    GIVEN a Flask application
    WHEN the '/' home page is requested (GET)
    THEN check the response is valid (200 status code)
    """
    response = client.get('/')
    assert response.status_code == 200


def test_index_content(client):
    """
        GIVEN a Flask application
        WHEN the '/' home page is requested
        THEN check the response contains "Calculator"
        """
    response = client.get('/')
    print(f'The response.data includes {response.data}.')
    assert 'Calculator' in str(response.data)


def test_response_data_add_is_correct(client):
    """
        GIVEN two terms have been entered correctly with the value 2 and Add is selected and the form submitted
        WHEN the form is submitted from the index page
        THEN check the response contains the correct result (4)
        """
    response = client.post('/result', data=dict(
        first_term=2,
        second_term=2,
        operation='Add'), follow_redirects=True)
    assert 'The result is: 4' in str(response.data)
