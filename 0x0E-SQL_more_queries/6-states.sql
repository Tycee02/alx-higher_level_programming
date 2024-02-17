-- create a database 'hbtn_0d_usa'
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table 'states' in the database 'hbtn_0d_usa'
-- description: id INT unique, auto generated, not null and primary key
-- name VARCHAR(256) not NULL

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id));
