from starlette import status


def test_main_returns_status_code_http_200_ok(client):
    response = client.get('/health')
    assert response.status_code == status.HTTP_200_OK


def test_main_works_ok(client):
    response = client.get('/health')
    expected = {'message': 'The API is 100% ok!'}

    assert response.json() == expected
