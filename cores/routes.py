from flask import Flask, request
from flask import current_app as app

from controllers.product import *
from controllers.client import *


@app.route('/api/clients', methods=['GET'])
def clients():
    """
    Get all clients in db
    """
    return get_all_clients()

@app.route('/api/products', methods=['GET'])
def movies():
    """
    Get all products in db
    """
    return get_all_products()

@app.route('/api/client', methods=['GET', 'POST', 'PUT', 'DELETE'])
def actor():
    if request.method == 'GET':
        return get_client_by_id()
    elif request.method == 'POST':
        return add_client()
    elif request.method == 'PUT':
        return update_client()
    elif request.method == 'DELETE':
        return delete_client()

@app.route('/api/product', methods=['GET', 'POST', 'PUT', 'DELETE'])
def movie():
    if request.method == 'GET':
        return get_product_by_id()
    elif request.method == 'POST':
        return add_product()
    elif request.method == 'PUT':
        return update_product()
    elif request.method == 'DELETE':
        return delete_product()

@app.route('/api/client-relations', methods=['PUT', 'DELETE'])
def actor_relations():
    if request.method == 'PUT':
        return client_add_relation()
    elif request.method == 'DELETE':
        return client_clear_relations()

@app.route('/api/product-relations', methods=['PUT', 'DELETE'])
def movie_relations():
    if request.method == 'PUT':
        return product_add_relation()
    elif request.method == 'DELETE':
        return product_clear_relations()