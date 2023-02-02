from service import procurar_service
from fastapi import status, Depends
from model.dto import ListagemDTO
from .router import router


#Procurando por categoria ou palavras [Todas por categoria ou palavras chaves]
@router.get('/procurar', status_code=status.HTTP_200_OK)
def procurar_controller(
    listagem_dto: ListagemDTO = Depends()
):
    return procurar_service(listagem_dto.__dict__,)
