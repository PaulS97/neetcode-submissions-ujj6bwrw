-- Write your query below
SELECT customers.name
FROM customers
WHERE customers.id NOT IN (select distinct customer_id from orders)