-- Drops the existing procedure if it already exists to avoid conflicts
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Sets the delimiter to allow for complete procedure definition
DELIMITER //

-- Creates the stored procedure to compute and update the weighted average score
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare a session variable to store the computed weighted average score
    SET @average := (SELECT
                         SUM(c.score * p.weight) / SUM(p.weight)
                     FROM corrections c
                     INNER JOIN projects p ON c.project_id = p.id
                     WHERE c.user_id = user_id
                     AND p.weight > 0);

    -- Update the users table with the calculated average
    UPDATE users SET average_score = @average WHERE id = user_id;
END //

-- Reset the delimiter to the default semicolon
DELIMITER ;
