from fastapi.responses import RedirectResponse
from repository import requisicao_repository
from fastapi import HTTPException


def listagem_service(dados: dict):
    print('Service')
    payload = {
        "dados": dados
    }

    response = requisicao_repository(
        'GET',
        params=payload
    )
    print(response)

    if response.status_code == 200:
        return RedirectResponse(response.json())

    raise HTTPException(
        status_code=404
    )
