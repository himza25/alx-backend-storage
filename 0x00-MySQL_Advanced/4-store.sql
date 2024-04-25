-- Trigger to decrease item quantity on new order
DROP TRIGGER IF EXISTS after_order_insert;
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
