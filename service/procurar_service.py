from repository import procurar_repository
from fastapi import HTTPException


def procurar_service(dto:dict):

    res = procurar_repository(dto)
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

    print(total)
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
