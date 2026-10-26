from pydantic import BaseModel, Field


class Level(BaseModel):
    """This class use pydantic for check width and height and
    pacgum for all livels"""
    width: int = Field(ge=9)
    height: int = Field(ge=7)
    pacgum: int = Field(ge=1)


class Config(BaseModel):
    """This class for check list of livels"""
    levels: list[Level]
