import pydantic

class ProductBase(pydantic.BaseModel):
  id: int
  nome_produto: str
  descricao: str
  preco: float
  estoque: int
  categoria_id: int
  created_at: str
  updated_at: str