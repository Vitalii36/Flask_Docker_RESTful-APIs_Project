use my_bd;

CREATE TABLE client (
    id INT NOT NULL AUTO_INCREMENT,
    code VARCHAR(20) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    source_id INT,
    PRIMARY KEY (id));
    
SHOW VARIABLES LIKE "secure_file_priv";
    
LOAD DATA INFILE '/var/lib/mysql-files/store-data_client.csv' 
INTO TABLE client 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM client;

CREATE TABLE product (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    price DECIMAL,
    PRIMARY KEY (id));

LOAD DATA INFILE '/var/lib/mysql-files/store-data_product.csv' 
INTO TABLE product 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM product;