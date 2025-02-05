import requests

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "4d36a1c36f9e079b69005d2530c5f03b"
HEADER = {"Comtent-Type" : "application/json",
          "trainer_token" : TOKEN
          }

body_createPokemon = {
    "name": "Cheizzi",
    "photo_id": 5
}

response = requests.post(url = f'{URL}pokemons', headers=HEADER, json = body_createPokemon)

print(response.text)

message = response.json()["message"]
print(message)