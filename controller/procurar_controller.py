from repository import procurar_repository
from model.dto import ListagemDTO
from .router import router
from fastapi import status, Depends


@router.get('/procurar')
def procurar_controller(
    listagem_dto: ListagemDTO = Depends()
):
    return procurar_repository(listagem_dto.__dict__,)
