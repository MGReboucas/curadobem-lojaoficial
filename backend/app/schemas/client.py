import pydantic

class ClientBase(pydantic.BaseModel):
  id: int
  nome_cliente: str
  email: str
  telefone: str
  cpf: str
  senha_hash: str
  aceitou_politica_privacidade: bool
  aceitou_termos_uso: bool
  email_verificado: bool
  status: str
  created_at: str
  updated_at: str