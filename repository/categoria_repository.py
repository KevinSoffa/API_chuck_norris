from requests import request
from decouple import config


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
    print(cat.json())
    return cat.json()
