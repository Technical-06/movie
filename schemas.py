from typing import Optional
from pydantic import BaseModel

class UserSchema(BaseModel):
    id:int
    username:str
    email:str

    class Config:
        orm_mode =True


class MovieSchema(BaseModel):
    id:int
    name:str
    description:str
    type:str
    rating:str

    class Config:
        orm_mode =True

class BookingkSchema(BaseModel):
    id:int
    movie_id:int
    user_id:int
    seat_type:str

    
    class Config:
        orm_mode =True

class SeatBookSchema(BaseModel):
    id:int
    seat_type:str
    user_id:int
    
    class Config:
        orm_mode =True



