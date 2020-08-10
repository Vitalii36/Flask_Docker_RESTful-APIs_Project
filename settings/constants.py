import os

# connection credentials ??? this PostgreSQL my mySQL
DB_URL =  os.environ['mysql+mysqldb://vitalii36:Pvs657864!@127.0.0.1[:3306]/my_bd'] #os.environ['DB_URL']

# entities properties
CLIENT_FIELDS = ['id', 'code', 'first_name', 'last_name', 'source-id']
PRODUCT_FIELDS = ['id', 'name', 'price']
