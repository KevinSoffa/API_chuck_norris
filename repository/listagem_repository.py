from fastapi import HTTPException
from requests import request
from decouple import config


#Random de Piadas
def requisicao_repository():

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
    return response
