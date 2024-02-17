-- create a database 'hbtn_0d_usa'
-- If the table states already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table 'cities' in the database 'hbtn_0d_usa'
-- description: id INT unique, auto generated, not null and primary key
--state_id INT, not null, foreign key and reference to id of states table
-- name VARCHAR(256) not NULL

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
    FOREIGN KEY (state_id)
        REFERENCES hbtn_0d_usa.states(id));
