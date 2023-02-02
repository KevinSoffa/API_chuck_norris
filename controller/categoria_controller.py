from service import categoria_service
from .router import router
from fastapi import status


#Lista de Categorias
@router.get('/categorias', status_code=status.HTTP_200_OK)
def categoria_controller():
    return categoria_service()
