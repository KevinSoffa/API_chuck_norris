from dataclasses import dataclass
from fastapi import Query


@dataclass
class ListagemDTO:
    paginacao_limite: int = Query(0)
    categoria: str = Query(...)
