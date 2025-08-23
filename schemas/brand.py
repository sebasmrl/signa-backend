from typing import Optional
from pydantic import BaseModel, Field

class Brand(BaseModel):
    id: Optional[int] = Field(
        default=None,
        description="id no es requerido",
        example=1
    )
    state:bool = Field(
        default=False,
        description="state no es requerido",
        example=1
    )
    owner: str
    brand: str
    