import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "4d36a1c36f9e079b69005d2530c5f03b"
HEADER = {"Comtent-Type" : "application/json",
          "trainer_token" : TOKEN
          }
TREAINER_ID = '21687'


def test_status_code():
    response = requests.get(url = f'{URL}pokemons', params = {'trainer_id' : TREAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}pokemons', params = {'trainer_id' : TREAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Arch'

@pytest.mark.parametrize('key, value', [('name', 'Arch'),('trainer_id', TREAINER_ID),('id', '205754')])
def test_parametrize(key, value): 
     response_parametrize = requests.get(url = f'{URL}pokemons', params = {'trainer_id' : TREAINER_ID})
     assert response_parametrize.json()['data'][0][key] == value