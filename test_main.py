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
