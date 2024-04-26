-- Drop the existing procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Set the delimiter to allow for complete procedure definition
DELIMITER //

-- Create the stored procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Declare a local variable to store the computed average score
    DECLARE calculated_avg FLOAT;

    -- Calculate the average score from the 'corrections' table where the 'user_id' matches
    SELECT AVG(score) INTO calculated_avg FROM corrections WHERE user_id = user_id;

    -- Debug: Output the calculated average to help ensure correct computation
    SELECT calculated_avg AS debug_calculated_avg;

    -- Check if there were any scores to calculate the average from
    IF calculated_avg IS NOT NULL THEN
        -- Update the 'average_score' in the 'users' table for the provided 'user_id'
        UPDATE users SET average_score = calculated_avg WHERE id = user_id;
    ELSE
        -- Optional: Handle cases where no scores are present if needed
        UPDATE users SET average_score = 0 WHERE id = user_id;
    END IF;
END //
DELIMITER ;
