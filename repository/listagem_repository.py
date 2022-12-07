from fastapi import HTTPException
from requests import request
from decouple import config


def requisicao_repository():
    print('repository')


    listagem = request(
        'GET',
        '%s/' % (
            config('URL')
        ),
        headers={
            'Content-Type': 'application/json'
        }
    )

    response = listagem.json()
    print(response)
    if response:
        return {
            "joker": response['value'],
        }
    raise HTTPException(
    status_code=404
    )
