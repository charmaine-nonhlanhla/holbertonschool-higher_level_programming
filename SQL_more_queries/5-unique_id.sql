-- Script to create the table 'unique_id' with specified columns

-- Create table 'unique_id' if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

