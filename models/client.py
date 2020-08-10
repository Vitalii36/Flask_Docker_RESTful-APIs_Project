from .base import Model
from core import db
from .relations import association


class Client(Model, db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    source_id = db.Column(db.Integer)
    # ?????^^^^^?????
    products = db.relationship('product', backref='store', uselist=True, secondary=client_has_product)
    # ?????^^^^^?????
    def __repr__(self):
        return '<Client {}>'.format(self.name)