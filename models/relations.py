from core import db

client_has_product = db.Table('client_has_product',
    db.Column('client_id', db.Integer, db.ForeignKey('clients.id', primary_key = True)),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id', primary_key = True))
)