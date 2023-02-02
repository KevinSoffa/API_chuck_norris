from service import random_categoria_service
from fastapi import status, Depends
from model.dto import ListagemDTO
from .router import router


#Procurando por categoria ou palavras piadas aleatorias
@router.get('/random/categoria', status_code=status.HTTP_200_OK)
def random_controller(
    listagem_dto: ListagemDTO = Depends()
):
    return random_categoria_service(listagem_dto.__dict__,)
