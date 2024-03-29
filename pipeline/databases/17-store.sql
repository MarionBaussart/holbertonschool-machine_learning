-- script that creates a trigger that decreases the quantity of an item after adding a new order
DELIMITER $$
CREATE TRIGGER update_stock
    AFTER INSERT ON orders
    FOR EACH ROW
    BEGIN
        UPDATE items
            SET quantity=quantity-New.number
            WHERE name=New.item_name;
    END $$
DELIMITER ;
