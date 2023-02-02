from repository import requisicao_repository
from fastapi import HTTPException



def listagem_service():

    response = requisicao_repository()

    if response:
        return {
            "api": "Chuck Norris",
            "joke": response['value'],
        }

    raise HTTPException(
        status_code=404
    )
