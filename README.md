# REST API Flask with MySLQ Database

## Motivation
Created REST API which can be used as a template for the following projects. 
Used a Flask, MySQL and the Docker and created a simple database on the basic of CVS file

## Database
MySQL database my_bd is created on the basis of CSV files from the course "Introduction to databases - https://stepik.org/course/551" and represents three tables: clients, products, 
client_has_product. The table of clients is connected by the relation many to many through the table client_has_product with products.

<div align="center">
    <img align="center" src="https://github.com/Vitalii36/Flask_Docker_RESTful-APIs_Project/blob/master/image_readme/Database_my_db.png?raw=true">
</div>

Before start we need write Database URL in constans.py like this
DB_URL = 'mysql+mysqldb://user:password@host:port/database_name' or export URL in terminal before
run app

## How to use
We should install pip install -r requirements.txt and MySQL

    click==7.1.2
    db-url==0.3.3
    Flask==1.1.2
    Flask-SQLAlchemy==2.4.4
    itsdangerous==1.1.0
    Jinja2==2.11.2
    MarkupSafe==1.1.1
    mysql-connector-python==8.0.21
    mysqlclient==2.0.1
    protobuf==3.12.4
    six==1.15.0
    SQLAlchemy==1.3.18
    Werkzeug==1.0.1

To test you need to download a repo clone or docker image - 'pull vitalii36 / api_store_pvs'. 
Also in the repo is a database and model MySQL Workbench for a full test
As you already know, the main idea of the project is to develop an API for interaction with the database. So, 
we'll be able to add/remove/update records via API routes.

We'll use the following routes methods:

    GET to retrieve information from the source
    POST to send data to the source
    PUT to replace (update) data
    DELETE to remove data
    
We'll have the following routes:

    /api/products, /api/clients to get the list of all products, clients from the DB, method: GET

    /api/client, to manipulate with the client's records, methods:
    
    GET: get client by id
    POST: add new client, body can include:
    'code', 'first_name', 'last_name', 'source-id'
    PUT: update client, body can include:
    'code', 'first_name', 'last_name', 'source-id'
    DELETE: remove client, body:
    id
    
    /api/product, to manipulate with the products records, methods:
    
    GET: get movie by id
    POST: add new product, body can include:
    'name', 'price'
    PUT: update product, body can include:
    'name', 'price'
    DELETE: remove product, body:
    id
    
    /api/client-relations to manipulate with client's relations, methods:
    
    PUT: add relations, body:
    id, relation_id
    DELETE: delete relations, body:
    id
    
    /api/product-relations to manipulate with product's relations, methods:
    
    PUT: add relations, body:
    id, relation_id
    DELETE: delete relations, body:
    id

## Start
If cloned repo, in the directory run from the terminal run.py, if the docker 

    sudo docker run -p 8000: 8000 --network host -e DB_URL = mysql + mysqldb: // user: password@0.0.0.0: 5432 / my_db my_app_api

user = your user name;  
password = your password;   
my_bd = name database;  
my_app_api = docker image;  

P.S.
If you have ERROR like "caching_sha2_password" you can use MySQL consol and you can
 change password encryption like this.

    ALTER USER 'yourusername' @ 'localhost' IDENTIFIED WITH mysql_native_password BY 'youpassword';

## Example
<div align="center">
    <img align="center" src="https://github.com/Vitalii36/Flask_Docker_RESTful-APIs_Project/blob/master/image_readme/Example_1.png?raw=true">
    <>
    <img align="center" src="https://github.com/Vitalii36/Flask_Docker_RESTful-APIs_Project/blob/master/image_readme/Example_2.png?raw=true">
    <>
    <img align="center" src="https://github.com/Vitalii36/Flask_Docker_RESTful-APIs_Project/blob/master/image_readme/Example_3.png?raw=true">

</div> 

## License
Format is MIT
