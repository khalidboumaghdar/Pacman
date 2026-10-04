from pydantic import BaseModel, Field


class Level(BaseModel):
    width: int = Field(ge=9)
    height: int = Field(ge=7)
    pacgum: int = Field(ge=1)


class Config(BaseModel):
    levels: list[Level]