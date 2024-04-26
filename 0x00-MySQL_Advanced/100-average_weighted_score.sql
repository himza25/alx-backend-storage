-- Drops the existing procedure if it already exists to avoid conflicts
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Sets the delimiter to allow for complete procedure definition
DELIMITER //

-- Creates the stored procedure to compute and update the weighted average score
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Variables to hold sums and counts
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE final_weighted_average FLOAT;

    -- Selecting and computing weighted scores and total weights
    SELECT SUM(c.score * p.weight) INTO total_weighted_score,
           SUM(p.weight) INTO total_weight
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculating the final weighted average if total weight is not zero
    IF total_weight > 0 THEN
        SET final_weighted_average = total_weighted_score / total_weight;
    ELSE
        SET final_weighted_average = 0;
    END IF;

    -- Updating the user's average score in the users table
    UPDATE users SET average_score = final_weighted_average WHERE id = user_id;
END //

-- Resetting the delimiter back to the semicolon
DELIMITER ;
