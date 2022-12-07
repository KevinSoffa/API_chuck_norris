from fastapi import HTTPException
from requests import request


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

    #filtrando por dados relevantes
    for value in res['result']:
        valores = {
            "api": "chucknorris",
            "category": value['categories'],
            "joker": value['value']
        }
        response.append(valores)

    #aplicando limitação
    limite = dto['paginacao_limite']
    total = len(response)

    if dto['paginacao_limite']:
        response = response[:limite]

        if dto['paginacao_limite'] > total:
            return {
                "error": 404,
                "detail": str(dto['paginacao_limite']) + f' é maior ao número total de piadas: {total}'
            } 
        return response

    if response:
        return response

    raise HTTPException(
    status_code=404
    )
