from repository import procurar_repository
from fastapi import status, Depends
from model.dto import ListagemDTO
from .router import router


#Procurando por categoria ou palavras
@router.get('/procurar', status_code=status.HTTP_200_OK)
def procurar_controller(
    listagem_dto: ListagemDTO = Depends()
):
    return procurar_repository(listagem_dto.__dict__,)
