from repository import procurar_repository
from model.dto import ListagemDTO
from .router import router
from fastapi import status, Depends


@router.get('/procurar', status_code=status.HTTP_200_OK)
def procurar_controller(
    listagem_dto: ListagemDTO = Depends()
):
    return procurar_repository(listagem_dto.__dict__,)
