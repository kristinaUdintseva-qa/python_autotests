import requests

base_url = "https://pokemonbattle.me:9104/"
TOKEN = "12dd9f7b7197fc88e0eb4fd2b2cfdebd"

# запрос на создание покемона
response_add_pokemon = requests.post(f"{base_url}pokemons", headers={"trainer_token" : TOKEN}, json={
    "name": "QA Mewtoo",
    "photo": "https://dolnikov.ru/pokemons/albums/091.png"
})

print(response_add_pokemon.text)

# запрос на изменение имени покемона
response_put_pokemon_name = requests.put(f"{base_url}pokemons", headers={"trainer_token" : TOKEN}, json={
    "pokemon_id": "8998",
    "name": "New Name Mewtoo",
    "photo": "https://dolnikov.ru/pokemons/albums/091.png"
})

print(response_put_pokemon_name.text)

# запрос на добавление покемона в покебол
response_add_pokeball = requests.post(f"{base_url}trainers/add_pokeball", headers={"trainer_token" : TOKEN}, json={
    "pokemon_id": "8998"
})

print(response_add_pokeball.text)