-- Creates database stack_dev_db
CREATE DATABASE IF NOT EXISTS stack_dev_db;
USE stack_dev_db;
CREATE USER IF NOT EXISTS 'stack_dev'@'localhost' IDENTIFIED BY 'stack_dev_pwd';
GRANT ALL ON stack_dev_db.* TO 'stack_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'stack_dev'@'localhost';
