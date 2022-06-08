from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__= "user"
    id=Column(Integer,primary_key=True,index=True)
    username = Column(String(255))
    email=Column(String(255))

class Movie(Base):
    __tablename__="movie"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(255))
    description=Column(String(255))
    type=Column(String(255))
    rating=Column(String(255))

class Booking(Base):
    __tablename__="booking"
    id=Column(Integer,primary_key=True,index=True)
    movie_id = Column(Integer,ForeignKey("movie.id"))
    user_id = Column(Integer,ForeignKey("user.id"))
    bookseat_type = Column(ForeignKey("bookseat.seat_type"))
    movie = relationship("Movie")
    user = relationship("User")
    bookseat = relationship("SeatBook")

class SeatBook(Base):
    __tablename__="bookseat"
    seat_id=Column(Integer,primary_key=True,index=True)
    seat_type=Column(String(255),nullable=False)
    user_id=Column(Integer,ForeignKey("user.id"))
    user = relationship("User")