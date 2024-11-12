import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '7857'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_name_trainer():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == "Шеф"