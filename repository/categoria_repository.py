from requests import request
from decouple import config


#Lista de categorias
def categoria_repository():
    #requisição na API
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

    return response
