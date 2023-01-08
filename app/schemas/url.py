from pydantic import BaseModel


class OriginUrl(BaseModel):
    origin_url: str


class ShortUrl(BaseModel):
    short_url: str
