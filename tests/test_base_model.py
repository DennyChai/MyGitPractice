from pydantic import BaseModel, StrictInt, Field, StrictStr


class Job(BaseModel):
  title: StrictStr
  on_board_date: StrictStr = Field(..., alias='onBoardDate')

class MyData(BaseModel):
  name: StrictStr
  age: StrictInt
  expire_time: StrictInt = Field(..., alias='expireTime')

