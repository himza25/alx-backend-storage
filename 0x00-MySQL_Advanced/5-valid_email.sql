-- Trigger to reset valid_email when email changes
DROP TRIGGER IF EXISTS before_email_update;
DELIMITER //
CREATE TRIGGER before_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END; //
DELIMITER ;
