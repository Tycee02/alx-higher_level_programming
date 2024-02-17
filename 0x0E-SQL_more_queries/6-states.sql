-- create a database 'hbtn_0d_usa'
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table 'states' (in the database)
-- description: id INT unique, auto generated, can't be null and is a primary key
-- name VARCHAR(256) can not be NULL

CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
