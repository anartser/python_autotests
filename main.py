import requests

URL =   'https://api.pokemonbattle.ru/v2'
TOKEN = '31cf6754374e1a3400aabf68242150ac'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registation)'''

''' response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message = response_create.json()[id]
print(message)
'''
body_rename = {
    "pokemon_id": "27563",
    "name": "Чермандер",
    "photo_id": 2
}

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

body_add_pokeball = {
    "pokemon_id": "27563"
}
response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)




