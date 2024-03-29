-- script that creates a trigger that resets the attribute valid_email only when the email has been changed
DELIMITER $$
CREATE TRIGGER reset_valid_email
    BEFORE UPDATE ON users
    FOR EACH ROW
    BEGIN
        IF New.email != Old.email THEN
            SET New.valid_email = NOT(Old.valid_email);
        END IF;
    END $$
DELIMITER ;
