from app import app
import json


def test_home_page():
    print('Home page testing is started.')
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Todo API - Developed by Utku Erdemir!" in response.data


def test_get_todos():
    print('Get todos testing is started.')
    response = app.test_client().get('/todos')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data['success']
    assert 'data' in data


def test_post_todos():
    print('Post todos testing is started.')
    response = app.test_client().post('/todos', data={'todo_name': 'sample todo'})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 201
    assert data['success']
    assert data['message'] == "Todo sample todo named is saved."


def test_post_empty_todo():
    print('Post empty todo testing is started.')
    response = app.test_client().post('/todos')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert not(data['success'])
    assert data['message'] == "Todo name cannot be empty."


def test_post_empty_string_todo():
    print('Post empty string todo testing is started.')
    response = app.test_client().post('/todos', data={'todo_name': ''})
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 400
    assert not(data['success'])
    assert data['message'] == "Todo name cannot be empty."
