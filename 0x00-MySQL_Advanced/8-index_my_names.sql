-- SQL script to create an index on the first letter of the name column in the names table

-- Drop existing index if it exists to avoid conflicts when recreating or updating the index
DROP INDEX IF EXISTS idx_name_first ON names;

-- Create a new index on the first letter of the name column
CREATE INDEX idx_name_first ON names (name(1));
