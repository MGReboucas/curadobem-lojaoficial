import pydantic

class categories(pydantic.BaseModel):
    id: int
    nome_categoria: str
    created_at: str
    updated_at: str