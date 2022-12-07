from fastapi import HTTPException
from requests import request
from decouple import config


#Lista de categorias
def categoria_repository():
    cat = request(
        'GET',
        '%s/' % (
            config('URL_CATEGORIA')
        ),
        headers={
            'Content-Type': 'application/json'
        }
    )

    response = cat.json()

    if response:
        return response

    raise HTTPException(
        status_code=404
    )
