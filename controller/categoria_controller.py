from repository import categoria_repository
from .router import router
from fastapi import status


@router.get('/categoria')
def categoria_controller():
    return categoria_repository()
