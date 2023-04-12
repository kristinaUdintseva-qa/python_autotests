import requests
import pytest

TOKEN = "12dd9f7b7197fc88e0eb4fd2b2cfdebd"

# Проверка, что ответ запрос GET /trainers приходит с кодом 200
def test_ststus_code():
    response = requests.get("https://pokemonbattle.me:9104/trainers", params={"trainer_id" : 3881})
    assert response.status_code == 200

# Проверка, что в ответе приходит строчка с именем тренера
def test_trainer_name():
    response = requests.get("https://pokemonbattle.me:9104/trainers", params={"trainer_id" : 3881})
    assert response.json()["trainer_name"] == "QA Kristina"