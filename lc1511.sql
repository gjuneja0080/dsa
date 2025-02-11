WITH purchases AS (
    SELECT 
        o.customer_id, 
        c.name, 
        MONTH(o.order_date) AS order_month, 
        SUM(o.quantity * p.price) AS amount_spent
    FROM orders o
    JOIN product p ON o.product_id = p.product_id
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.order_date BETWEEN '2020-06-01' AND '2020-07-31'
    GROUP BY o.customer_id, c.name, MONTH(o.order_date)
)
SELECT customer_id, name
FROM purchases
WHERE (order_month = 6 AND amount_spent >= 100)
   OR (order_month = 7 AND amount_spent >= 100)
GROUP BY customer_id, name
HAVING COUNT(DISTINCT order_month) = 2;
