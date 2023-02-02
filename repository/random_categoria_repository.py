from fastapi import HTTPException
from requests import request
import random


# Filtro por palavra e categoria
def random_repository(dto: dict):
    procurar = request(
        'GET',
        'https://api.chucknorris.io/jokes/search?query=' + dto['categoria'],
        headers={
            'Content-Type': 'application/json'
        }
    )

    res = procurar.json()

    return res
