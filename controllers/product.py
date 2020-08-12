from flask import jsonify, make_response
from models import Client, Product
from settings.constants import PRODUCT_FIELDS
from .parse_request import get_request_data


def get_all_products():
    """
    Get list of all records
    """
    all_product = Product.query.all()
    products = []
    for product in all_product:
        prod = {k: v for k, v in product.__dict__.items() if k in PRODUCT_FIELDS}
        products.append(prod)
    return make_response(jsonify(products), 200)


def get_product_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Product.query.filter_by(id=row_id).first()
        try:
            product = {k: v for k, v in obj.__dict__.items() if k in PRODUCT_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(product), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def add_product():
    """
    Add new product
    """
    data = get_request_data()
    if 'name' in data.keys():
        try:
            new_record = Product.create(**data)
        except:
            err = 'Incorrect data format'
            return make_response(jsonify(error=err), 400)
        new_product = {k: v for k, v in new_record.__dict__.items() if k in PRODUCT_FIELDS}
        return make_response(jsonify(new_product), 200)
    else:
        err = 'No name specified'
        return make_response(jsonify(error=err), 400)


def update_product():
    """
    Update product record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if Product.query.filter_by(id=data['id']).first() == None:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        if 'name' in data.keys():
            if Product.query.filter_by(name=data['name']).first() != None:
                product = Product.query.filter_by(name=data['name']).first()
                err = {k: v for k, v in product.__dict__.items() if k == 'id'}
                row_id = int(err['id'])

        for key in data.keys():
            if key not in PRODUCT_FIELDS:
                err = 'fields does not exist in Product table'
                return make_response(jsonify(error=err), 400)

        try:
            new_record = Product.update(row_id, **data)
        except:
            err = 'Incorrect data format'
            return make_response(jsonify(error=err), 400)
        new_product = {k: v for k, v in new_record.__dict__.items() if k in PRODUCT_FIELDS}
        return make_response(jsonify(new_product), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def delete_product():
    """
    Delete product by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
        index = Product.delete(row_id)
        if index == 1:
            msg = 'Record successfully deleted'
            return make_response(jsonify(message=msg), 200)
        else:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def product_add_relation():
    """
    Add client to product's cast
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if 'relation_id' in data.keys():
            try:
                rel_id = int(data['relation_id'])
            except:
                err = 'relation_id must be integer'
                return make_response(jsonify(error=err), 400)

            if Client.query.filter_by(id=rel_id).first() != None:
                rel_obj = Client.query.filter_by(id=rel_id).first()
            else:
                err = 'Record with such relation_id does not exist'
                return make_response(jsonify(error=err), 400)

            try:
                product = Product.add_relation(row_id, rel_obj)
            except:
                err = 'Record with such id does not exist'
                return make_response(jsonify(error=err), 400)

            rel_product = {k: v for k, v in product.__dict__.items() if k in PRODUCT_FIELDS}
            rel_product['Client'] = str(product.Client)
            return make_response(jsonify(rel_product), 200)

        else:
            err = 'No relation-id specified'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def product_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        try:
            product = Product.clear_relations(row_id) # clear relations here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        rel_product = {k: v for k, v in product.__dict__.items() if k in PRODUCT_FIELDS}
        rel_product['Client'] = str(product.Client)
        return make_response(jsonify(rel_product), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)