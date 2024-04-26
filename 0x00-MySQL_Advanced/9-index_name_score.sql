-- SQL script to create a composite index on the first letter of the name and the score

-- Drop existing index if it exists to avoid conflicts when recreating or updating the index
DROP INDEX IF EXISTS idx_name_first_score ON names;

-- Create a composite index on the first letter of the name and the score
CREATE INDEX idx_name_first_score ON names (name(1), score);
