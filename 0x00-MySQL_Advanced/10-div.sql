-- Drop the existing function if it already exists to avoid conflicts
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the new function SafeDiv
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    -- Check if the second argument, b, is zero
    IF b = 0 THEN
        -- Return 0 if b is zero to avoid division by zero
        SET result = 0;
    ELSE
        -- Perform division a / b if b is not zero
        SET result = a / b;
    END IF;
    -- Return the result of the division or 0
    RETURN result;
END //

DELIMITER ;
