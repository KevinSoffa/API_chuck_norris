from fastapi import HTTPException
from requests import request
from decouple import config


#Random de Piadas
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

    if response:
        return {
            "api": "Chuck Norris",
            "joke": response['value'],
        }

    raise HTTPException(
        status_code=404
    )
