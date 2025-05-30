from sqlalchemy import *
from  extentions import db

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False ,index=true)
    password =Column(String, nullable=False,index=true)
    phone = Column(String(11), nullable=False,index=true)
    address = Column(String, nullable=False,index=true)
