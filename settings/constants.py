import os

# connection credentials
DB_URL =  os.environ['DB_URL']
# before run api you need export DB_URL=mysql+mysqldb://user:password@host:port/database_name in consol
# DB_URL = 'mysql+mysqldb://user:password@host:port/database_name' # if you know your DB

# entities properties
CLIENT_FIELDS = ['id', 'code', 'first_name', 'last_name', 'source-id']
PRODUCT_FIELDS = ['id', 'name', 'price']
