import requests 
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9c9b1ddaf79d0c2833f949c6bf2535cb'
HEADER = {'Content-Type' : 'applikation/json', 'trainer_token':TOKEN}
TRAINER_ID = '6570'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
      response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
      assert response_get.json()[ "data"][0]["trainer_name"] == 'Shu' 