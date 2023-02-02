from repository import categoria_repository
from fastapi import HTTPException


def categoria_service():

    response = categoria_repository()

    if response:
        return response

    raise HTTPException(
        status_code=404
    )
