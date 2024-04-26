-- Drops the existing procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Resets the delimiter to allow for the entire procedure to be defined as a single command
DELIMITER //

-- Creates the stored procedure to compute and update the average score
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Declare a session variable to store the computed average score
    SET @user_avg = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);

    -- Update the average_score field in the users table for the specified user_id
    UPDATE users SET average_score = @user_avg WHERE id = user_id;
END //
DELIMITER ;
