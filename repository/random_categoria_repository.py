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

    response = []

    #filtrando por Categoria ou palavras
    for value in res['result']:

        valores = {
            "category": value['categories'],
            "joke": value['value']
        }
        response.append(valores)

    #aplicando limitação
    limite = dto['paginacao_limite']
    total = len(response)
    
    aleatorio = random.randint(0, int(total))
    

    if dto['paginacao_limite']:
        response = response[:limite]

        if dto['paginacao_limite'] > total:
            raise HTTPException(
                status_code=404,
                detail=str(dto['paginacao_limite']) + f' é maior ao número total de piadas: {total}'
            )

        return response
    
    if response:
        if total == aleatorio:
            aleatorio = aleatorio - 1
            return {
                "response": response[aleatorio]
            }

        return {
            "response": response[aleatorio]
        }

    raise HTTPException(
    status_code=404
    )
