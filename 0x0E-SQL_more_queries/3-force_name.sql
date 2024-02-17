-- Create the table force_name
-- with the description id INT, name VARCHAR(256) can not be null
-- if the table force_name already exists, your script should not fail

CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL);
