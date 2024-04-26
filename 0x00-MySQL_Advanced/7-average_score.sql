-- Drops the existing procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Creates a new stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Declare a variable to store the computed average score
    DECLARE avg_score FLOAT;

    -- Compute the average score for the given user_id
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;

    -- Update the average_score in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END //
DELIMITER ;
