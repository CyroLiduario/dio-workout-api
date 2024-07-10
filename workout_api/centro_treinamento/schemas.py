from workout_api.contrib.schemas import BaseSchemas
from pydantic import UUID4, Field
from typing import Annotated

class CentroTreinamentoIn(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do Centro de Treinamento", example="CT Gralha", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do Centro de Treinamento", example="Avenida dos Alfeneiros, 4", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do Centro de Treinamento", example="João da Graça", max_length=30)]

class CentroTreinamentoAtleta(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do CT", example="CT Gralha", max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador da CT")]