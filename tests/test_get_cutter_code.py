from unittest.mock import patch

from starlette import status


@patch('api.main.gen_cutter_code')
def test_get_cutter_code_status_code_200_ok(mock_cutter_code, client):
    mock_cutter_code.return_value = 'P579'
    response = client.get('/v1/cutter/Piaget')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'P579'
