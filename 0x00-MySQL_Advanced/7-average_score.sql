-- Drops the existing stored procedure if it exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Recreate the stored procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT DEFAULT 0;

    -- Compute the average score if there are corrections, otherwise leave as default 0
    SELECT IFNULL(AVG(score), 0) INTO avg_score FROM corrections WHERE user_id = user_id;

    -- Update the average score in the users table
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END; //
DELIMITER ;
