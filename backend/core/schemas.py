from pydantic import BaseModel, ConfigDict


def to_camel(string: str) -> str:
    return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(string.split('_')))


class Schemas(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)