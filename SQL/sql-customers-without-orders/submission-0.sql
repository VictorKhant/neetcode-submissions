-- Write your query below
SELECT name FROM customers WHERE id not in (SELECT customer_id FROM orders)