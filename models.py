from sqlalchemy import Column,Integer,String,Float,Date
from db import Base,engine


class Weight(Base):
    __tablename__="Weight_entries"
    id = Column(Integer,primary_key=True)
    username = Column(String)
    weight=Column(Float)
    date=Column(Date)

class User(Base):
    __tablename__="Users"
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    password = Column(String)
    height=Column(Integer)



Base.metadata.create_all(bind=engine)