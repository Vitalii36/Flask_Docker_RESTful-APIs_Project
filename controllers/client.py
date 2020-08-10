from flask import jsonify, make_response
from models import Client, Product
from settings.constants import CLIENT_FIELDS
from .parse_request import get_request_data

def get_all_clients():
    """
    Get list of all records
    """
    all_clients = Client.query.all()
    clients = []
    for client in all_clients:
        act = {k: v for k, v in client.__dict__.items() if k in CLIENT_FIELDS}
        clients.append(act)
    return make_response(jsonify(clients), 200)

def get_client_by_id():
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

        obj = Client.query.filter_by(id=row_id).first()
        try:
            client = {k: v for k, v in obj.__dict__.items() if k in CLIENT_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(client), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def add_client():
    """
    Add new client
    """
    data = get_request_data()
    if 'name' in data.keys():

        try:
            new_record = Client.create(**data)
        except:
            err = 'Incorrect data format'
            return make_response(jsonify(error=err), 400)
        new_client = {k: v for k, v in new_record.__dict__.items() if k in CLIENT_FIELDS}
        return make_response(jsonify(new_client), 200)
    else:
        err = 'No name specified'
        return make_response(jsonify(error=err), 400)

def update_client():
    """
    Update client record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if Client.query.filter_by(id=data['id']).first() == None:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        if 'name' in data.keys():
            if Client.query.filter_by(name=data['name']).first() != None:
                client = Client.query.filter_by(name=data['name']).first()
                err = {k: v for k, v in client.__dict__.items() if k == 'id'}
                row_id = int(err['id'])

        for key in data.keys():
            if key not in CLIENT_FIELDS:
                err =  'fields does not exist in Client table'
                return make_response(jsonify(error=err), 400)

        try:
            new_record = Client.update(row_id, **data)
        except:
            err = 'Incorrect data format'
            return make_response(jsonify(error=err), 400)
        new_client = {k: v for k, v in new_record.__dict__.items() if k in CLIENT_FIELDS}
        return make_response(jsonify(new_client), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def delete_client():
    """
    Delete client by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)
        index = Client.delete(row_id)
        if index == 1:
            msg = 'Record successfully deleted'
            return make_response(jsonify(message=msg), 200)
        else:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def client_add_relation():
    """
    Add a product to client's store
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

            if Product.query.filter_by(id=rel_id).first() != None:
                rel_obj = Product.query.filter_by(id=rel_id).first()
            else:
                err = 'Record with such relation_id does not exist'
                return make_response(jsonify(error=err), 400)

            try:
                client = Client.add_relation(row_id, rel_obj)
            except:
                err = 'Record with such id does not exist'
                return make_response(jsonify(error=err), 400)

            rel_client = {k: v for k, v in client.__dict__.items() if k in CLIENT_FIELDS}
            rel_client['price'] = str(client.price)
            return make_response(jsonify(rel_client), 200)

        else:
            err = 'No relation-id specified'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def client_clear_relations():
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
            client = Client.clear_relations(row_id) # clear relations here
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        rel_client = {k: v for k, v in client.__dict__.items() if k in CLIENT_FIELDS}
        rel_client['filmography'] = str(client.price)
        return make_response(jsonify(rel_client), 200)
    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)