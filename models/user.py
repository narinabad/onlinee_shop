from sqlalchemy import *
from  extentions import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False ,index=true)
    password =Column(String, nullable=False,index=true)
    phone = Column(String(11), nullable=False,index=true)
    address = Column(String, nullable=False,index=true)
