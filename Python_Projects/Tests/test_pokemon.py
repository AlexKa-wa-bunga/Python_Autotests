import requests
import pytest
import json

def test_status_code():
    response = requests.get('https://pokemonbattle.me:9104/pokemons')
    assert response.status_code == 200

def test_json_contains_trainer_name():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id': '3339'})
    assert response.json()['trainer_name'] == 'AlexKa_Wa_Bunga'

