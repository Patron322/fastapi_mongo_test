from pydantic import BaseModel


class FormResponseNotFound(BaseModel):
    field_name_1: str
    field_name_2: str


class FormResponse(BaseModel):
    name: str
