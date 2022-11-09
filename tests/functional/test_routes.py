# Write tests for al routes
from iebank_api import app
import pytest


def test_get_accounts(testing_client):
    
    response = testing_client.get('/accounts')
    assert response.status_code == 200


def test_dummy_wrong_path():
    
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404


def test_create_account(testing_client):
    
    response = testing_client.post(
        '/accounts', json={'name': 'Joe Doe', 'currency': '€'})
    assert response.status_code == 200
    assert response.json['name'] == 'Joe Doe'
    assert response.json['currency'] == '€'


def test_delete_account(testing_client):

    response = testing_client.delete('/accounts/1')
    assert response.status_code == 200


def test_update_account(testing_client):

    update = testing_client.put(
        '/accounts/1', json={'name': 'Joe Doe', 'currency': '€'})
    assert update.status_code == 200
    assert update.json['name'] == 'Joe Doe'
    assert update.json['currency'] == '€'


def get_account(testing_client):
    response = testing_client.get('/accounts/1')
    assert response.status_code == 200
    assert response.json['name'] == 'Joe Doe'
    assert response.json['currency'] == '€'
