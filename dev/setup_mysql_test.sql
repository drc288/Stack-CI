-- Creates database stack_test_db
CREATE DATABASE IF NOT EXISTS stack_test_db;
USE stack_test_db;
CREATE USER IF NOT EXISTS 'stack_test'@'localhost' IDENTIFIED BY 'stack_test_pwd';
GRANT ALL PRIVILEGES ON stack_test_db.* TO 'stack_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'stack_test'@'localhost';
