from typing import Literal
import requests
import pytest

URL =   'https://api.pokemonbattle.ru/v2'
TOKEN = '31cf6754374e1a3400aabf68242150ac'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = '4371'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'

def test_part_of_response1():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_id'] == TRAINER_ID

@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '42532')])
def test_parametrize (key: Literal['name'] | Literal['trainer_id'] | Literal['id'], value: Literal['Бульбазавр'] | Literal[4371] | Literal[42417]):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value