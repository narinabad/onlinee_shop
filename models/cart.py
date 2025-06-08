from sqlalchemy import *
from  extentions import db

class Cart(db.Model):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeinKey('users.id'),nullable=False)
    status= Column(String, default='pending')
    user=db.relationship('User', backref='carts')
