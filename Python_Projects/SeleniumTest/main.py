import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'aad126132031eb6072d51fd507861a02'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Автозавр",
    "photo_id": 1
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name = {
    "pokemon_id": pokemon_id,
    "name": "Autozavr2",
    "photo_id": 5
}

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)