import re
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Union

from pydantic import BaseModel, field_validator


class AbstractValidator(ABC):
   
    @abstractmethod
    def valid(cls):
        pass


class MixinType:

    @classmethod
    def type(cls):
        return cls.__name__


class Phone(AbstractValidator, BaseModel, MixinType):
    phone: str

    @field_validator('phone')
    @classmethod
    def valid(cls, value: str) -> Union[str, None]:
        if (isinstance(value, str) and len(value) == 12 and value[1::].isdigit() and value[1] == '7'):
            return value
        return None


class Email(AbstractValidator, BaseModel, MixinType):
    email: str

    @field_validator('email')
    @classmethod
    def valid(cls, value: str) -> Union[str, None]:
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, value):
            return value
        else:
            return


class Date(AbstractValidator, BaseModel, MixinType):
    date: str

    @field_validator('date')
    @classmethod
    def valid(cls, value: str) -> Union[str, None]:
        try:
            value = datetime.strptime(value, "%d.%m.%Y")
            return value
        except ValueError:
            try:
                value = datetime.strptime(value, "%Y.%m.%d")
                return value
            except ValueError:
                return None


class FieldNameValidator:
    __validators = [Date, Phone, Email]

    def __call__(self, value: str) -> str:
        for validator in self.__validators:
            if validator.valid(value):
                return validator.type()
        if len(value) > 1:
            return 'String'
        return 'null'


field_type = FieldNameValidator()
