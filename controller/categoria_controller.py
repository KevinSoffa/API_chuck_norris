from repository import categoria_repository
from .router import router
from fastapi import status


@router.get('/categorias', status_code=status.HTTP_200_OK)
def categoria_controller():
    return categoria_repository()
