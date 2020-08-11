from .base import Model
from core import db
from .relations import client_has_product

class Product(Model, db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique = True, nullable=False)
    price = db.Column(db.Float(11))
    # ?????^^^^^?????
    clients = db.relationship('client', backref='price', uselist=True, secondary=client_has_product)
    # ?????^^^^^?????
    def __repr__(self):
        return '<Product {}>'.format(self.name)