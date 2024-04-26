-- Drops the existing procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Changes the delimiter to define the stored procedure
DELIMITER //

-- Creates the stored procedure to compute and update the average score
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Calculate the average score using a session variable
    SET @user_avg = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
    
    -- Update the users table with the calculated average score
    UPDATE users SET average_score = @user_avg WHERE id = user_id;
END //
DELIMITER ;
