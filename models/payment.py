from sqlalchemy import *
from  extentions import db

class Payment(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeinKey('carts.id'),nullable=False)
    status= Column(String, default='pending')
    cart=db.relationship('Carts', backref='payments')
