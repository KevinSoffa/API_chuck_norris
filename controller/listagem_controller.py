from repository import requisicao_repository
from .router import router
from fastapi import status


#Piadas Aleatorias
@router.get('', status_code=status.HTTP_200_OK)
def listagem_controller():
    return requisicao_repository()
