-- Creates the table force_name on your MySQL server
-- with the description id INT, name VARCHAR(256) can not be null
-- if the table force_name already exists, your script should not fail

CREATE TABLE force_name IF NOT EXISTS(
    id INT,
    name VARCHAR(256) NOT NULL);
    