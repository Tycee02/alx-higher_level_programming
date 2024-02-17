-- Creates the MySQL server user_0d_1
-- It should have all priviledges on your MySQL srver
-- The password should be set to user_0d_pwd

CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
