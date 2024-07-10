from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchemas, OutMixin
from pydantic import Field, PositiveFloat
from typing import Annotated, Optional

class Atleta(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do Atleta", example="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF", example="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="Idade", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso", example=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura", example=1.70)]
    genero: Annotated[str, Field(description="Gênero", example="M", max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do Atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="CT do Atleta")]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchemas):
    nome: Annotated[Optional[str], Field(None, description="Nome do Atleta", example="João", max_length=50)]
    idade: Annotated[Optional[int], Field(None, description="Idade", example=25)]