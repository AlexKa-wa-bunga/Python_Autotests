import requests
import json

# protocol = 'https://'
# host = 'pokemonbattle.me:9104'
trainer_token = 'вствь_свой_токен'

response = requests.post('https://pokemonbattle.me:9104/pokemons', json = {
    "name": "Пикаааа Чууууу 2",
    "photo": "https://www.clipartmax.com/png/middle/348-3480957_cavemantraining-build-fire-with-friction-10-things-pika-pikachu.png"
}, headers = {'trainer_token': trainer_token})

print(response.text)

pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": pokemon_id,
    "name": "Пикачуха",
    "photo": ""
}, headers = {'trainer_token': trainer_token})

print(response_change.text)

response_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": pokemon_id
}, headers = {'trainer_token': trainer_token})

print(response_pokeball.text)
