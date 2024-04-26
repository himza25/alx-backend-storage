-- Drops the existing procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Sets the delimiter to allow for complete procedure definition
DELIMITER //

-- Creates the stored procedure to compute and update the weighted average score
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare variables to hold the total weighted score and the sum of weights
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weights INT;
    
    -- Calculate the total weighted score and the total weights for the specified user
    SELECT SUM(c.score * p.weight) INTO total_weighted_score,
           SUM(p.weight) INTO total_weights
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Check if there are any weights to avoid division by zero
    IF total_weights > 0 THEN
        -- Update the average score in the users table with the weighted average
        UPDATE users SET average_score = (total_weighted_score / total_weights) WHERE id = user_id;
    ELSE
        -- If no weights, set average score to zero to handle cases with no corrections or weights
        UPDATE users SET average_score = 0 WHERE id = user_id;
    END IF;
END //

-- Reset the delimiter to the default semicolon
DELIMITER ;
