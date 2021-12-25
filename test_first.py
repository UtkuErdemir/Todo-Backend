from app import app


def test_home_page_with_fixture():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data