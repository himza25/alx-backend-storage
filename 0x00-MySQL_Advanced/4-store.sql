-- Ensures the trigger for decreasing item quantity is robust against multiple scenarios
DROP TRIGGER IF EXISTS after_order_insert;
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END; //
DELIMITER ;
