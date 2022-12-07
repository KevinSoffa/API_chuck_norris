from repository import requisicao_repository
from .router import router
from fastapi import status


@router.get('')
def listagem_controller():
    return requisicao_repository()
