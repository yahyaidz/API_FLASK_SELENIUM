import pytest
from app import app  # Import your Flask app instance


@pytest.fixture(scope="module")
def test_client():
    """
    Fixture to initialize the Flask test client.
    """
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


def test_navigate(test_client):
    """
    Test for the navigate action.
    """
    url = 'https://amazon.com'
    response = test_client.post('/execute_instructions', json={'actions': [{'type': 'navigate', 'url': url}]})
    data = response.get_json()

    assert response.status_code == 200
    assert data['result'][0] == {'message': f'Navigated to {url}'}


def test_click(test_client):
    """
    Test for the click action.
    """
    url = 'https://amazon.com'
    selector = "#nav-signin-tooltip > a > span"
    response = test_client.post('/execute_instructions', json={
        'actions': [{'type': 'navigate', 'url': url}, {'type': 'click', 'selector': selector}]})
    data = response.get_json()

    assert response.status_code == 200
    assert data['result'] == [{'message': f'Navigated to {url}'},
                              {'message': f'Clicked element with selector {selector}'}]


def test_screenshot(test_client):
    """
    Test for the screenshot action.
    """
    url = 'https://amazon.com'
    response = test_client.post('/execute_instructions',
                                json={'actions': [{'type': 'navigate', 'url': url}, {'type': 'screenshot'}]})
    data = response.get_json()

    assert response.status_code == 200
    assert data['result'] == [{'message': f'Navigated to {url}'}, {'message': 'Saved screenshot as screenshot.png'}]


def test_execute_script(test_client):
    """
    Test for the execute_script action.
    """
    url = 'https://amazon.com'
    response = test_client.post('/execute_instructions', json={
        'actions': [{'type': 'navigate', 'url': url}, {'type': 'execute_script', 'script': 'return document.title;'}]})
    data = response.get_json()

    assert response.status_code == 200
    assert data['result'] == [{'message': f'Navigated to {url}'},
                              {'script_result': 'Amazon.com. Spend less. Smile more.'}]
