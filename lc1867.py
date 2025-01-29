WITH avg_quant_mets AS (
    SELECT 
        order_id, 
        SUM(quantity) / COUNT(DISTINCT product_id) AS avg_quant_order, 
        MAX(quantity) AS max_quant
    FROM OrdersDetails
    GROUP BY order_id
),

max_vs_avg AS (
    SELECT DISTINCT a1.order_id
    FROM avg_quant_mets a1
    WHERE a1.max_quant > (SELECT MAX(a2.avg_quant_order) FROM avg_quant_mets a2)
)

SELECT order_id FROM max_vs_avg;
