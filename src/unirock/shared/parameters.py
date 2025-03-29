from typing import Annotated, Self, Any
from fastapi import Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, PositiveInt, ValidationError, model_validator, Field


class LimitOffsetParamDto(BaseModel):
    limit: PositiveInt
    offset: int = Field(ge=0)

    @model_validator(mode='before')
    @classmethod
    def both_present_or_none(cls, data: Any) -> Any:
        limit = data.get("limit")
        offset = data.get("offset")
        is_only_limit = limit is not None and offset is None
        is_only_offset = limit is None and offset is not None
        if is_only_limit or is_only_offset:
            raise ValueError("You should specify both limit and offset.")
        return data


def get_limit_offset_params(limit: int | None = None, offset: int | None = None):
    if limit is None and offset is None:
        return None
    try:
        dto = LimitOffsetParamDto(limit=limit, offset=offset)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=[
            {
                "type": error["type"],
                "msg": error["msg"],
                "input": error["input"],
                "url": error["url"]
            }
            for error in e.errors()])

    return dto


LimitOffsetParams = Annotated[LimitOffsetParamDto | None, Depends(get_limit_offset_params)]
