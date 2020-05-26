import main
from unittest.mock import patch


@patch('main.requests.get')
def test_server_is_online(get_mock):
    get_mock.return_value.status_code = 200
    lat = -14.235004
    lng = -51.92528
    response = main.get_response(lat, lng)
    status = response.status_code
    assert status == 200


@patch('main.requests.get')
def test_server_is_offline(get_mock):
    get_mock.return_value.status_code = 500
    lat = -14.235004
    lng = -51.92528
    response = main.get_response(lat, lng)
    status = response.status_code
    assert status == 500


@patch('main.requests.get')
def test_positive_latitude(get_mock):
    temperature = {"currently": {"temperature": 86}}
    get_mock.return_value.json.return_value = temperature
    lat = 60
    lng = 0
    result = 30
    response = main.get_temperature(lat, lng)
    assert response == result


@patch('main.requests.get')
def test_negative_lng(get_mock):
    temperature = {"currently": {"temperature": 75.20}}
    get_mock.return_value.json.return_value = temperature
    lat = 0
    lng = -150
    result = 24
    response = main.get_temperature(lat, lng)
    assert response == result
