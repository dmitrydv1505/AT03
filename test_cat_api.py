import pytest
import requests
from requests.exceptions import RequestException
from cat_api import get_random_cat_image


def test_get_random_cat_image_success(mocker):
    # Mock the response from requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    mocker.patch('requests.get', return_value=mock_response)

    url = get_random_cat_image()
    assert url == 'https://example.com/cat.jpg'


def test_get_random_cat_image_failure(mocker):
    # Mock the response to simulate a failed request (e.g., 404 not found)
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = []

    mocker.patch('requests.get', return_value=mock_response)

    url = get_random_cat_image()
    assert url is None


def test_get_random_cat_image_exception(mocker):
    # Simulate a request exception
    mocker.patch('requests.get', side_effect=RequestException)

    url = get_random_cat_image()
    assert url is None