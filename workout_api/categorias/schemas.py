from workout_api.contrib.schemas import BaseSchemas
from pydantic import UUID4, Field
from typing import Annotated

class CategoriaIn(BaseSchemas):
    nome: Annotated[str, Field(description="Nome da Categoria", example="Scale", max_length=10)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador da Categoria")]