-- Drops the existing stored procedure if it exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Set the delimiter to handle complex stored procedure statements
DELIMITER //

-- Create the stored procedure ComputeAverageScoreForUser
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Declare a variable to hold the computed average score
    DECLARE user_avg FLOAT;

    -- Calculate the average score from the corrections table
    SELECT AVG(score) INTO user_avg FROM corrections WHERE user_id = user_id;

    -- Check if the average score is NULL, which can happen if no scores exist, and set it to 0 in that case
    SET user_avg = IFNULL(user_avg, 0);

    -- Update the average_score in the users table with the calculated average or 0 if no scores were present
    UPDATE users SET average_score = user_avg WHERE id = user_id;
END //
DELIMITER ;
