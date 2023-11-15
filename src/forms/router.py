from typing import Union

from fastapi import APIRouter, Query

from mongo import client as mongo
from utils import field_type

from forms.models import FormResponse, FormResponseNotFound

router = APIRouter(
    prefix='/forms',
    tags=['Формы']
)


@router.post('/get_form')
async def get_form(
    field_name_1: str = Query(default=''),
    field_name_2: str = Query(default='')) -> Union[FormResponse, FormResponseNotFound]:
    cursor = mongo.find({"$or": [
                        {"field_name_1": {"$in": [field_name_1, field_name_2]}},
                        {"field_name_2": {"$in": [field_name_1, field_name_2]}}]},
                            {'_id': 0, "field_name_1": 0, "field_name_2": 0}).limit(1)
    form = await cursor.to_list(length=1)
    if not form:
        return FormResponseNotFound(
            field_name_1=field_type(field_name_1),
            field_name_2=field_type(field_name_2))
    return FormResponse(**form[0])
