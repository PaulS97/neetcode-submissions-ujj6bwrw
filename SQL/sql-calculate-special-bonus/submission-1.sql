-- Write your query below
SELECT 
    employee_id, 
    CASE
        WHEN SUBSTR(name, 1, 1) != 'M' and employee_id % 2 = 1 THEN salary
        ELSE 0 
    END as bonus
    FROM employees
    ORDER BY employee_id

