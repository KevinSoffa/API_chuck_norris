from model.dto import ListagemDTO
from fastapi import status, Depends
from .router import router
from repository import random_repository


#Procurando por categoria ou palavras
@router.get('/random/categoria', status_code=status.HTTP_200_OK)
def random_controller(
    listagem_dto: ListagemDTO = Depends()
):
    return random_repository(listagem_dto.__dict__,)
