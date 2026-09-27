from pydantic import BaseModel, Field



class Level(BaseModel):
    width: int = Field(ge=9)
    height: int = Field(ge=7)
    pacgum: int = Field(ge=1)
    
    # @model_validator(mode="before")
    # @classmethod
    # def check_dict(cls, data_dict: dict) -> dict:
    #     if


class Config(BaseModel):
    levels: list[Level]