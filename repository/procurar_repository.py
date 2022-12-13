from fastapi import HTTPException
from requests import request
import random


# Filtro por palavra e categoria
def procurar_repository(dto: dict):
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
    
    a = random.randint(0, int(total))
    print('RANDOM: ',a)

    if dto['paginacao_limite']:
        response = response[:limite]

        if dto['paginacao_limite'] > total:
            raise HTTPException(
                status_code=404,
                detail=str(dto['paginacao_limite']) + f' é maior ao número total de piadas: {total}'
            )
        print('com limitação')
        return response
    
    if response:
        return {
            "total": total,
            "response": response
        }

    raise HTTPException(
    status_code=404
    )
