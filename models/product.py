from sqlalchemy import *
from  extentions import db

class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False ,index=true)
    discription = Column(String(11), nullable=False, index=true)
    price=Column(Integer, nullable=False,index=true)


    address = Column(String, nullable=False,index=true)A
