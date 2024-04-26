-- Drops the existing procedure if it already exists to avoid conflicts
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Sets the delimiter to allow for complete procedure definition
DELIMITER //

-- Creates the stored procedure to compute and update the weighted average score for all users
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Temporary table to store intermediate results
    CREATE TEMPORARY TABLE IF NOT EXISTS TempScores (
        user_id INT,
        weighted_average FLOAT
    );

    -- Calculate the weighted scores for each user and store them in the temporary table
    INSERT INTO TempScores (user_id, weighted_average)
    SELECT c.user_id, SUM(c.score * p.weight) / SUM(p.weight)
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    GROUP BY c.user_id;

    -- Update the users table with the calculated averages from the temporary table
    UPDATE users u
    JOIN TempScores t ON u.id = t.user_id
    SET u.average_score = t.weighted_average;

    -- Drop the temporary table after use
    DROP TABLE TempScores;
END //

-- Reset the delimiter to the default semicolon
DELIMITER ;
