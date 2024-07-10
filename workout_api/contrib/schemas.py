from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class BaseSchemas(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True

class OutMixin(BaseSchemas):
    id: Annotated[UUID4, Field(description="Identificador")]
    created_at: Annotated[datetime, Field(description="Data de Criação")]
