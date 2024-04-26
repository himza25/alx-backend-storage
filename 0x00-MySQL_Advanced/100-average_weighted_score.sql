-- Create the stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare variables to store scores and weights
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;

    -- Calculate the sum of weighted scores and total weight
    SELECT 
        SUM(c.score * p.weight) INTO total_score,
        SUM(p.weight) INTO total_weight
    FROM 
        corrections c
    JOIN 
        projects p ON c.project_id = p.id
    WHERE 
        c.user_id = user_id;

    -- Update the average_score in the users table with the weighted average
    UPDATE users
    SET average_score = CASE 
                            WHEN total_weight > 0 THEN total_score / total_weight
                            ELSE 0
                        END
    WHERE id = user_id;
END //
DELIMITER ;
