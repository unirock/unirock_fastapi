import decimal
from xml.etree.ElementTree import Element

from pydantic import BaseModel, RootModel


class CbrCurrencyValueResponseDto(BaseModel):
    cbr_id: str
    num_code: str
    char_code: str
    nominal: int
    name: str
    value: decimal.Decimal

class CbrCurrencyValueList(RootModel):
    root: list[CbrCurrencyValueResponseDto]

    @classmethod
    def from_xml(cls, tree: Element) -> 'CbrCurrencyValueList':
        ...