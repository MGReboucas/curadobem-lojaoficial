import pydantic

class Address(pydantic.BaseModel):
    id: int
    street: str
    city: str
    state: str
    zip_code: str
    created_at: str
    updated_at: str